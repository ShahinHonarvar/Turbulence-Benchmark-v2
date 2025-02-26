def palindrome_of_length_n(s):
    s = s.lower()
    palindromes = set()
    n = len(s)
    for start in range(n - 26):
        substring = s[start:start + 27]
        if len(substring) == 27 and substring.isalpha() and (substring == substring[::-1]):
            palindromes.add(substring)
    return palindromes