import re

def palindromes_of_specific_lengths(s):
    substring = s[15:87].lower()
    english_letters = re.sub('[^a-z]', '', substring)
    length_range = range(51, 61)
    palindromes = set()
    for length in length_range:
        for i in range(len(english_letters) - length + 1):
            chunk = english_letters[i:i + length]
            if chunk == chunk[::-1]:
                palindromes.add(chunk)
    return palindromes