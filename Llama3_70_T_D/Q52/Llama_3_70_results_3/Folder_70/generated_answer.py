def palindrome_of_length_n(s):

    def is_palindrome(sub):
        return sub.lower() == sub[::-1].lower()
    s = ''.join(filter(str.isalpha, s))
    return set((sub for i in range(len(s) - 400) for sub in [s[i:i + 401]] if is_palindrome(sub)))