def palindrome_of_length_at_least_n(s):

    def is_palindrome(substr):
        return substr.lower() == substr.lower()[::-1]
    palindromes = set()
    s = s.lower()
    for length in range(6, len(s) + 1):
        for start in range(len(s) - length + 1):
            substr = s[start:start + length]
            if is_palindrome(substr) and substr.isalpha():
                palindromes.add(substr)
    return palindromes