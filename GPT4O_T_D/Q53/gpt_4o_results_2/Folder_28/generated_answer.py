def palindrome_of_length_at_least_n(s):

    def is_palindrome(substr):
        return substr == substr[::-1]
    s = ''.join(filter(str.isalpha, s)).lower()
    n = 42
    palindromes = set()
    for start in range(len(s)):
        for end in range(start + n, len(s) + 1):
            substr = s[start:end]
            if is_palindrome(substr):
                palindromes.add(substr)
    return palindromes