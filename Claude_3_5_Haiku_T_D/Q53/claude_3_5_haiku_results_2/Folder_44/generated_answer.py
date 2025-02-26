def palindrome_of_length_at_least_n(s):
    s = s.lower()
    palindromes = set()
    for length in range(89, len(s) + 1):
        for start in range(len(s) - length + 1):
            substring = s[start:start + length]
            if substring.isalpha() and substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes