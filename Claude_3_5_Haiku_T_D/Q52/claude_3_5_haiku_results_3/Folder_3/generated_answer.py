def palindrome_of_length_n(s):
    s = s.lower()
    palindromes = set()
    n = len(s)
    for i in range(n - 99):
        substring = s[i:i + 100]
        if len(substring) == 100 and substring == substring[::-1] and substring.isalpha():
            palindromes.add(substring)
    return palindromes