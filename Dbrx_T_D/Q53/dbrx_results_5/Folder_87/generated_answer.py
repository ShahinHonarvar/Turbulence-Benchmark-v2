def palindrome_of_length_at_least_n(s):

    def is_palindrome(s):
        s = ''.join((c.lower() for c in s if c.isalpha()))
        return s == s[::-1]
    return {s[i:j] for i in range(len(s)) for j in range(i + 18, len(s) + 18) if is_palindrome(s[i:j])}