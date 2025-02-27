def palindrome_of_length_at_least_n(s):

    def is_palindrome(s):
        return s.lower() == s.lower()[::-1]
    res = set()
    for i in range(len(s)):
        for j in range(17, len(s) - i + 1):
            sub = s[i:i + j]
            if is_palindrome(sub):
                res.add(sub)
    return res