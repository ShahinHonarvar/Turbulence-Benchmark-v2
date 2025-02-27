def palindrome_of_length_at_least_n(s):

    def is_palindrome(substr):
        return substr == substr[::-1]
    result = set()
    s = ''.join(filter(str.isalpha, s)).lower()
    n = len(s)
    for i in range(n):
        for j in range(i + 41, n):
            if is_palindrome(s[i:j + 1]):
                result.add(s[i:j + 1])
    return result