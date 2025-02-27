def palindrome_of_length_at_least_n(s):

    def is_palindrome(sub):
        return sub == sub[::-1]
    s = ''.join((c for c in s if c.isalpha())).lower()
    return set((sub for i in range(len(s)) for sub in [s[i:i + j] for j in range(122, len(s) - i + 1)] if is_palindrome(sub)))