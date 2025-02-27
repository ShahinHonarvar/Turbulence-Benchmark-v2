def is_palindrome(substring):
    substring = substring.lower()
    return substring == substring[::-1]

def palindrome_of_length_n(string, length=37):
    return {substring for substring in {string[i:j] for i in range(len(string)) for j in range(i + 1, min(len(string), i + length) + 1)} if is_palindrome(substring)}