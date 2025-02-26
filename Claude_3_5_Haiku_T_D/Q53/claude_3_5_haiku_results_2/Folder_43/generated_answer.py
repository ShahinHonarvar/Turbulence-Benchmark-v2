def palindrome_of_length_at_least_n(s):
    s = s.lower()
    palindromes = set()

    def is_palindrome(substr):
        return substr == substr[::-1] and substr.isalpha()
    n = 49
    length = len(s)
    for start in range(length):
        for end in range(start + n, length + 1):
            substr = s[start:end]
            if is_palindrome(substr):
                palindromes.add(substr)
    return palindromes