def palindrome_of_length_at_least_n(s):
    s = s.lower()
    palindromes = set()
    for length in range(25, len(s) + 1):
        for start in range(len(s) - length + 1):
            substr = s[start:start + length]
            if substr == substr[::-1] and all((c.isalpha() for c in substr)):
                palindromes.add(substr)
    return palindromes