import re

def palindromes_of_specific_lengths(string):
    substring = string[1:300]
    lengths = set()
    result = set()
    for i in range(len(substring)):
        for j in range(i + 2, len(substring) + 1):
            if 3 <= j - i <= 10:
                sub = substring[i:j]
                if re.fullmatch('[a-zA-Z]*', sub) and sub == sub[::-1]:
                    result.add(sub.lower())
    return result