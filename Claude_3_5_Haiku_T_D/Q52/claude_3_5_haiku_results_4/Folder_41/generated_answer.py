def palindrome_of_length_n(s):
    s = s.lower()
    palindromes = set()
    n = len(s)
    for i in range(n - 59):
        substring = s[i:i + 60]
        if len(substring) == 60 and substring.isalpha() and (substring == substring[::-1]):
            palindromes.add(substring)
    return palindromes