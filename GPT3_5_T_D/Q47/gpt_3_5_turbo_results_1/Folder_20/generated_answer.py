import re

def palindromes_of_specific_lengths(string):
    substring = string[20:75]
    palindromes = set()
    for length in range(36, 43):
        for i in range(len(substring) - length + 1):
            sub = substring[i:i + length]
            sub = re.sub('[^a-zA-Z]', '', sub)
            if sub.lower() == sub.lower()[::-1]:
                palindromes.add(sub.lower())
    return palindromes