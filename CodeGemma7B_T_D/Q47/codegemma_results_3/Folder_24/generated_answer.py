import re

def palindromes_of_specific_lengths(text):
    pattern = re.compile('(?i)\\\\b\\\\w{42,77}\\\\b')
    result = set()
    for word in pattern.findall(text[12:93]):
        if word == word[::-1]:
            result.add(word)
    return result