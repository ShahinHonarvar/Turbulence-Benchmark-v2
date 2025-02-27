import re

def palindromes_of_specific_lengths(s):

    def is_palindrome(substring):
        return substring == substring[::-1]
    substring = s[103:277].lower()
    english_letters = re.sub('[^a-z]', '', substring)
    palindromes = set()
    for length in range(100, 170):
        for i in range(len(english_letters) - length + 1):
            candidate = english_letters[i:i + length]
            if is_palindrome(candidate):
                palindromes.add(candidate)
    return palindromes