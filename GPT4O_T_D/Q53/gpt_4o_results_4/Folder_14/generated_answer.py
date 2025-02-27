def palindrome_of_length_at_least_n(s):

    def is_palindrome(sub):
        return sub == sub[::-1]
    s = ''.join(filter(str.isalpha, s)).lower()
    n = len(s)
    result = set()
    for length in range(13, n + 1):
        for start in range(n - length + 1):
            substr = s[start:start + length]
            if is_palindrome(substr):
                result.add(substr)
    return result