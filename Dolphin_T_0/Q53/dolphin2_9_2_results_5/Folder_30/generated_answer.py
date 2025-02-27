def palindrome_of_length_at_least_n(s):

    def is_palindrome(s):
        return s == s[::-1]

    def is_english_letters(s):
        return all((c.isalpha() for c in s))
    s = s.lower()
    n = 16
    return {s[i:j] for i in range(len(s)) for j in range(i + n, len(s) + 1) if is_palindrome(s[i:j]) and is_english_letters(s[i:j])}