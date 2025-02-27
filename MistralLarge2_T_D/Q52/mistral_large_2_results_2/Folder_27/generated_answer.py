def palindrome_of_length_n(s):

    def is_palindrome(substring):
        return substring.lower() == substring.lower()[::-1]
    n = 56
    return {s[i:i + n] for i in range(len(s) - n + 1) if is_palindrome(s[i:i + n]) and s[i:i + n].isalpha()}