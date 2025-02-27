def palindrome_of_length_at_least_n(s):

    def is_palindrome(sub):
        sub = sub.lower()
        return sub == sub[::-1]
    result = set()
    s = ''.join(filter(str.isalpha, s))
    n = len(s)
    for i in range(n):
        for j in range(i + 76, n + 1):
            substring = s[i:j]
            if is_palindrome(substring):
                result.add(substring.lower())
    return result