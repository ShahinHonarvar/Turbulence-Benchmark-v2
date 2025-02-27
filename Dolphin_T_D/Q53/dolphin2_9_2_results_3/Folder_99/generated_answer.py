def palindrome_of_length_at_least_n(s):

    def is_palindrome(s):
        return s == s[::-1]
    s = ''.join(filter(str.isalpha, s.lower()))
    return {s[i:j + 115] for i in range(len(s) - 114) for j in range(i + 114, len(s) + 1) if is_palindrome(s[i:j + 115])}