def palindrome_of_length_at_least_n(s):
    s = ''.join((c.lower() for c in s if c.isalpha()))
    n = len(s)
    result = set()

    def is_palindrome(sub):
        return sub == sub[::-1]
    for i in range(n):
        for j in range(i + 45, n + 1):
            substring = s[i:j]
            if is_palindrome(substring):
                result.add(substring)
    return result