def palindrome_of_length_at_least_n(s):

    def is_palindrome(substr):
        return substr.lower() == substr.lower()[::-1]
    palindromes = set()
    s_lower = s.lower()
    for length in range(59, len(s) + 1):
        for start in range(len(s) - length + 1):
            substr = s_lower[start:start + length]
            if is_palindrome(substr) and substr.replace(' ', '').isalpha():
                palindromes.add(substr)
    return palindromes