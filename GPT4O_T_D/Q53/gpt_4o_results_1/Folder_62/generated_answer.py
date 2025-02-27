def palindrome_of_length_at_least_n(s):

    def is_palindrome(subs):
        return subs == subs[::-1]
    s = ''.join(filter(str.isalpha, s)).lower()
    n = len(s)
    result = set()
    for length in range(31, n + 1):
        for start in range(n - length + 1):
            substring = s[start:start + length]
            if is_palindrome(substring):
                result.add(substring)
    return result