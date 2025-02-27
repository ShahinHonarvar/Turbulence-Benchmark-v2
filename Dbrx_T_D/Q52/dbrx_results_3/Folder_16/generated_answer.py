def palindrome_of_length_n(string, n=255):

    def is_palindrome(substring):
        substring = substring.lower()
        return substring == substring[::-1]
    return {substring for substring in {string[i:j] for i in range(len(string)) for j in range(i + n, len(string) + 1)} if is_palindrome(substring)}