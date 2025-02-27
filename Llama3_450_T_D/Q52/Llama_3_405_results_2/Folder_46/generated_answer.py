def palindrome_of_length_n(s):

    def is_palindrome(sub):
        return sub.lower() == sub.lower()[::-1]
    return set((sub for i in range(len(s) - 463) for sub in [s[i:i + 464]] if sub.isalpha() and is_palindrome(sub)))