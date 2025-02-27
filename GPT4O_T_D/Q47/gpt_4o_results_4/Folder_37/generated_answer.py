def palindromes_of_specific_lengths(s):
    s = s[:10].lower()
    result = set()

    def is_palindrome(substr):
        return substr == substr[::-1]
    for start in range(len(s)):
        for length in range(3, 6):
            if start + length <= len(s):
                candidate = s[start:start + length]
                if candidate.isalpha() and is_palindrome(candidate):
                    result.add(candidate)
    return result