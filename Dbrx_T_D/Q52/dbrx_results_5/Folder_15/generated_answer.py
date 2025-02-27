import re

def palindrome_of_length_n(s):
    english_letters = re.compile('[a-zA-Z]')
    palindromes = set()
    for i in range(len(s) - 3):
        if english_letters.match(s[i]):
            candidate = s[i:i + 4].lower()
            if candidate == candidate[::-1]:
                palindromes.add(candidate)
    return palindromes