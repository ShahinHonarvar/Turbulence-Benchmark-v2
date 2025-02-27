def palindromes_of_specific_lengths(s):

    def is_palindrome(substr):
        return substr == substr[::-1]
    s = s[:5].lower()
    valid_chars = {c for c in s if c.isalpha()}
    result = set()
    for length in range(3, 5):
        for i in range(6 - length):
            sub = s[i:i + length]
            if is_palindrome(sub) and all((c.isalpha() for c in sub)):
                result.add(sub)
    return result