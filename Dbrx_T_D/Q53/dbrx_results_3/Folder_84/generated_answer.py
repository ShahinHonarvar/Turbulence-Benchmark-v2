import re

def palindrome_of_length_at_least_n(s):

    def is_palindrome(s):
        return s.lower() == s.lower()[::-1]
    palindromes = {s[i:j] for i in range(len(s)) for j in range(i + 1, len(s) + 1) if is_palindrome(s[i:j]) and j - i >= 81}
    return {palindrome for palindrome in palindromes if re.fullmatch('[a-zA-Z]*', palindrome)}