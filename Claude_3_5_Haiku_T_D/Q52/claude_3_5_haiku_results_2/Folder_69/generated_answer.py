def palindrome_of_length_n(s):
    s = s.lower()
    palindromes = set()
    for start in range(len(s) - 471):
        substring = s[start:start + 472]
        if len(substring) == 472 and substring.isalpha() and (substring == substring[::-1]):
            palindromes.add(substring)
    return palindromes