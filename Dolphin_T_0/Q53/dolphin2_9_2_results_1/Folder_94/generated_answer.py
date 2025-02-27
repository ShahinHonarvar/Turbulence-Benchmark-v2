def palindrome_of_length_at_least_n(s):

    def is_palindrome(s):
        return s == s[::-1]

    def get_palindromes(s, n):
        return set((s[i:j + 1] for i in range(len(s) - n + 1) for j in range(i + n - 1, len(s)) if is_palindrome(s[i:j + 1])))
    return get_palindromes(s.lower(), 41)