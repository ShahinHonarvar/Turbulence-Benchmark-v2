def palindrome_of_length_n(s):
    s = s.lower()
    palindromes = set()
    for i in range(len(s)):
        for length in range(420, 0, -1):
            if i + length <= len(s):
                substr = s[i:i + length]
                if substr == substr[::-1] and all((c.isalpha() for c in substr)):
                    palindromes.add(substr)
    return palindromes