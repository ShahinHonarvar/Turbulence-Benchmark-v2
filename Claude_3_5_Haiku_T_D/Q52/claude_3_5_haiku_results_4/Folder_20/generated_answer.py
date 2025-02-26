def palindrome_of_length_n(s):
    s = s.lower()
    palindromes = set()
    for start in range(len(s) - 52):
        substring = s[start:start + 53]
        if len(substring) == 53 and substring.isalpha() and (substring == substring[::-1]):
            palindromes.add(substring)
    return palindromes