import re

def palindrome_of_length_n(s):

    def is_palindrome(sub):
        return sub == sub[::-1]
    n = 85
    palindromes = set()
    for i in range(len(s) - n + 1):
        substring = re.sub('[^a-zA-Z]', '', s[i:i + n]).lower()
        if len(substring) == n and is_palindrome(substring):
            palindromes.add(substring)
    return palindromes