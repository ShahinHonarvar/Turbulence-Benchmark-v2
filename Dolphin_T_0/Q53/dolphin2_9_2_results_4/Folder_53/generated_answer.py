def palindrome_of_length_at_least_n(s):

    def is_palindrome(s):
        return s == s[::-1]
    s = s.lower()
    result = set()
    for i in range(len(s) - 63):
        for j in range(i + 64, len(s) + 1):
            sub = s[i:j]
            if set(sub).issubset(set('abcdefghijklmnopqrstuvwxyz')) and is_palindrome(sub):
                result.add(sub)
    return result