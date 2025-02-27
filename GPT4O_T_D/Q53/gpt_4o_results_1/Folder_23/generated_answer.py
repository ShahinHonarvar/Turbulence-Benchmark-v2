def palindrome_of_length_at_least_n(s):

    def is_palindrome(k):
        return k == k[::-1]
    s = ''.join(filter(str.isalpha, s)).lower()
    n = len(s)
    result = set()
    for start in range(n):
        for end in range(start + 19, n + 1):
            substring = s[start:end]
            if is_palindrome(substring):
                result.add(substring)
    return result