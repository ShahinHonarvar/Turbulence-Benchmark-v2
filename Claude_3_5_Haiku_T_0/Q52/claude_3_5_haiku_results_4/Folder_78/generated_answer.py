def palindrome_of_length_n(s):
    s = s.lower()
    palindromes = set()
    n = len(s)
    for i in range(n - 47):
        substring = s[i:i + 48]
        if len(substring) == 48 and substring == substring[::-1] and substring.isalpha():
            palindromes.add(substring)
    return palindromes