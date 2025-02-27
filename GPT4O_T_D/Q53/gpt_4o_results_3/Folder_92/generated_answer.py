def palindrome_of_length_at_least_n(s):
    s = ''.join(filter(str.isalpha, s)).lower()
    n = len(s)
    result = set()

    def is_palindrome(subs):
        return subs == subs[::-1]
    for i in range(n):
        for j in range(i + 10, n + 1):
            substring = s[i:j]
            if is_palindrome(substring):
                result.add(substring)
    return result