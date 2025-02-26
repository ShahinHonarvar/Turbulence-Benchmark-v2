def palindrome_of_length_n(s):
    s = s.lower()
    palindromes = set()
    n = len(s)
    for i in range(n - 26):
        substring = s[i:i + 27]
        if len(substring) == 27 and substring.isalpha() and (substring == substring[::-1]):
            palindromes.add(substring)
    return palindromes