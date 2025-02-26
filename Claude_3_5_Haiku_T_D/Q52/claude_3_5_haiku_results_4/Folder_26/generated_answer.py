def palindrome_of_length_n(s):
    s = s.lower()
    palindromes = set()
    n = len(s)
    for i in range(n - 365):
        substring = s[i:i + 366]
        if len(substring) == 366 and substring == substring[::-1] and substring.isalpha():
            palindromes.add(substring)
    return palindromes