def palindrome_of_length_at_least_n(s):
    s = ''.join((c.lower() for c in s if c.isalpha()))
    n = len(s)
    result = set()

    def is_palindrome(substr):
        return substr == substr[::-1]
    for i in range(n):
        for j in range(i + 21, n + 1):
            substr = s[i:j]
            if is_palindrome(substr):
                result.add(substr)
    return result