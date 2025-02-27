def palindrome_of_length_at_least_n(s):

    def is_palindrome(s):
        return s == s[::-1]
    res = set()
    for i in range(len(s)):
        for j in range(i + 48, len(s) + 1):
            candidate = s[i:j].lower()
            if is_palindrome(candidate):
                if all((c in 'abcdefghijklmnopqrstuvwxyz' for c in candidate)):
                    res.add(candidate)
    return res