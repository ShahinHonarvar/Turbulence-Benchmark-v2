def palindrome_of_length_at_least_n(s):

    def is_palindrome(s):
        return s == s[::-1]
    s = ''.join((c for c in s if c.isalpha()))
    s = s.lower()
    result = set()
    for i in range(len(s)):
        for j in range(i + 15, len(s) + 1):
            subs = s[i:j]
            if is_palindrome(subs):
                result.add(subs)
    return result