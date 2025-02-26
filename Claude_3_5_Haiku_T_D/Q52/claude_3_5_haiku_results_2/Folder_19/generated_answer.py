def palindrome_of_length_n(s):
    s = s.lower()
    palindromes = set()
    n = len(s)
    if n < 67:
        return palindromes
    for i in range(n - 66):
        substring = s[i:i + 67]
        if len(substring) == 67 and substring.isalpha() and (substring == substring[::-1]):
            palindromes.add(substring)
    return palindromes