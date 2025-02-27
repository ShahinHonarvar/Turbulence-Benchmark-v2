def palindrome_of_length_n(s):

    def is_palindrome(sub):
        return sub == sub[::-1]
    s = ''.join(filter(str.isalpha, s)).lower()
    return {s[i:i + 93] for i in range(len(s) - 92) if is_palindrome(s[i:i + 93])}