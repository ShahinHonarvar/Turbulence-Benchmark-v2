def palindrome_of_length_n(s):

    def is_palindrome(sub):
        return sub == sub[::-1] and sub.isalpha()
    s = s.lower()
    return {s[i:i + 38] for i in range(len(s) - 38 + 1) if is_palindrome(s[i:i + 38])}