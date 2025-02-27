import re

def palindrome_of_length_n(s):
    s = s.lower()

    def is_palindrome(substring):
        substring = re.findall('[a-zA-Z]', substring)
        return substring == substring[::-1]
    return {substring for substring in {s[i:j] for i in range(len(s)) for j in range(i + 1, len(s) + 1)} if is_palindrome(substring) and len(substring) == 472}