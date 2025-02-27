def palindrome_of_length_n(s):

    def is_palindrome(substring):
        return substring.lower() == substring.lower()[::-1]
    length = 47
    return {s[i:i + length] for i in range(len(s) - length + 1) if is_palindrome(s[i:i + length]) and s[i:i + length].isalpha()}