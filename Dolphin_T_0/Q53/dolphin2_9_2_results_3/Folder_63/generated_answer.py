def palindrome_of_length_at_least_n(s):

    def is_palindrome(s):
        return s == s[::-1]
    s = s.lower()
    return set(filter(is_palindrome, [s[i:i + 37] for i in range(len(s) - 37 + 1)]))