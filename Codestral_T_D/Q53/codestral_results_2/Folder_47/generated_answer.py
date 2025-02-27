def palindrome_of_length_at_least_n(s):

    def is_palindrome(s):
        return s == s[::-1] and s.isalpha()
    s = s.lower()
    return {s[i:j] for i in range(len(s)) for j in range(i + 77, len(s) + 1) if is_palindrome(s[i:j])}