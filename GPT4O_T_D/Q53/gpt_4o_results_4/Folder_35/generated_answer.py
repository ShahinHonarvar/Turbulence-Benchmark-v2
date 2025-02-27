def palindrome_of_length_at_least_n(s):

    def is_palindrome(substr):
        return substr == substr[::-1]
    s = ''.join(filter(str.isalpha, s)).lower()
    start = 0
    palindromes = set()
    while start < len(s):
        for end in range(start + 26, len(s) + 1):
            candidate = s[start:end]
            if is_palindrome(candidate):
                palindromes.add(candidate)
        start += 1
    return palindromes