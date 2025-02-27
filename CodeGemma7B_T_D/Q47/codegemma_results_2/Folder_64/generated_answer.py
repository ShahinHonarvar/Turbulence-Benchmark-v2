import re

def palindromes_of_specific_lengths(word):
    pattern = re.compile('[a-zA-Z]{4,5}')
    result = set()
    for i in range(8):
        for j in range(i, 8):
            substring = word[i:j + 1]
            if pattern.fullmatch(substring):
                result.add(substring.lower())
    return result