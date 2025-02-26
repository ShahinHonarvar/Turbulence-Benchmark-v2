def palindrome_of_length_at_least_n(s):
    s = s.lower()
    palindromes = set()
    length = len(s)
    for start in range(length):
        for end in range(start + 1, length + 1):
            substring = s[start:end]
            if len(substring) >= 89 and substring.isalpha() and (substring == substring[::-1]):
                palindromes.add(substring)
    return palindromes