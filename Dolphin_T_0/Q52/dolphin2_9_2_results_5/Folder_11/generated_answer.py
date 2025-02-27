def palindrome_of_length_n(s):
    s = s.lower()

    def is_palindrome(s):
        return s == s[::-1]
    return {s[i:i + 77] for i in range(len(s) - 76) if is_palindrome(s[i:i + 77]) and s[i:i + 77].isalpha()}