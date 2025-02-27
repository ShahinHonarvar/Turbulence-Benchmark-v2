def palindrome_of_length_at_least_n(s):

    def is_palindrome(substr):
        return substr == substr[::-1]
    palindromes = set()
    s = ''.join(filter(str.isalpha, s.lower()))
    n = len(s)
    for i in range(n):
        for j in range(i + 140, n + 1):
            substr = s[i:j]
            if is_palindrome(substr):
                palindromes.add(substr)
    return palindromes