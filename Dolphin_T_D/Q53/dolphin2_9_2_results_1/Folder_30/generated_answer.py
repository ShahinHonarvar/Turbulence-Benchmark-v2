def palindrome_of_length_at_least_n(s):

    def is_palindrome(s):
        return s.lower() == s.lower()[::-1]
    s = ''.join((ch for ch in s if ch.isalpha()))
    return {s[i:j] for i in range(len(s)) for j in range(i + 16, len(s) + 1) if is_palindrome(s[i:j])}