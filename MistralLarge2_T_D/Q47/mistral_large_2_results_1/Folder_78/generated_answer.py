import re

def palindromes_of_specific_lengths(s):
    substring = s[15:73].lower()
    english_letters = re.findall('[a-z]+', substring)
    palindromes = set()
    for word in english_letters:
        length = len(word)
        if 19 <= length <= 55 and word == word[::-1]:
            palindromes.add(word)
    return palindromes