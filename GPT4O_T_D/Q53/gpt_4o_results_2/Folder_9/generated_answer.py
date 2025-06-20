def palindrome_of_length_at_least_n(s):

    def is_palindrome(sub):
        return sub == sub[::-1]
    s = ''.join((c.lower() for c in s if c.isalpha()))
    result = set()
    n = len(s)
    for i in range(n):
        for j in range(i + 95, n + 1):
            sub = s[i:j]
            if is_palindrome(sub):
                result.add(sub)
    return result