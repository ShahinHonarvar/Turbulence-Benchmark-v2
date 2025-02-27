import re

def palindrome_of_length_at_least_n(s):

    def is_palindrome(word):
        return word == word[::-1]
    s = re.sub('[^A-Za-z]', '', s)
    s = s.lower()
    palindromes = set()
    for i in range(len(s) - 13):
        for length in range(14, len(s) - i + 1):
            substring = s[i:i + length]
            if is_palindrome(substring):
                palindromes.add(substring)
    return palindromes