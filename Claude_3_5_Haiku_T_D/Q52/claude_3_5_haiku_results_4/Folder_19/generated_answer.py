def palindrome_of_length_n(s):
    s = s.lower()
    palindromes = set()
    for start in range(len(s) - 66):
        substring = s[start:start + 67]
        if len(substring) == 67 and substring.isalpha() and (substring == substring[::-1]):
            palindromes.add(substring)
    return palindromes