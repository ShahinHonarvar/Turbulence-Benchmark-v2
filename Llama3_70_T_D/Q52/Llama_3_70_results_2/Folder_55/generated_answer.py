def palindrome_of_length_n(s):

    def is_palindrome(sub):
        return sub.lower() == sub.lower()[::-1]
    s = s.lower()
    return set((sub for i in range(len(s) - 96) for sub in [s[i:i + 97]] if sub.isalpha() and is_palindrome(sub)))