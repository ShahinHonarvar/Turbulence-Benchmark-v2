def palindrome_of_length_at_least_n(s):

    def is_palindrome(substr):
        return substr == substr[::-1]
    s = ''.join(filter(str.isalpha, s)).lower()
    n = 55
    palindromes = set()
    for i in range(len(s)):
        for j in range(i + n - 1, len(s)):
            substr = s[i:j + 1]
            if is_palindrome(substr):
                palindromes.add(substr)
    return palindromes