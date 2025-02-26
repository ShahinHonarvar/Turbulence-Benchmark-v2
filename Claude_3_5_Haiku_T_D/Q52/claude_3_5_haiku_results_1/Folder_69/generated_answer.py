def palindrome_of_length_n(s):
    s = s.lower()
    palindromes = set()
    n = len(s)
    for start in range(n - 471):
        substring = s[start:start + 472]
        if len(substring) == 472 and substring.isalpha() and (substring == substring[::-1]):
            palindromes.add(substring)
    return palindromes