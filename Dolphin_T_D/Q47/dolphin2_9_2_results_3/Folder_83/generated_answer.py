import re

def palindromes_of_specific_lengths(s):
    substring = s[75:96]
    substring = re.sub('[^A-Za-z]', '', substring)
    palindromes = set()
    for length in range(7, 10):
        for i in range(len(substring) - length + 1):
            word = substring[i:i + length].lower()
            if word == word[::-1]:
                palindromes.add(word)
    return palindromes