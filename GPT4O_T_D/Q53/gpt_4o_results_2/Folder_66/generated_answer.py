def palindrome_of_length_at_least_n(s):

    def is_palindrome(substr):
        return substr == substr[::-1]
    n = 76
    s = ''.join(filter(str.isalpha, s)).lower()
    palindromes = set()
    for length in range(n, len(s) + 1):
        for start in range(len(s) - length + 1):
            substr = s[start:start + length]
            if is_palindrome(substr):
                palindromes.add(substr)
    return palindromes