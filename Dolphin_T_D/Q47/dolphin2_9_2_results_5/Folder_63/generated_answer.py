import re

def palindromes_of_specific_lengths(string):
    substring = string[33:86]
    palindromes = set()
    for length in range(26, 32):
        for i in range(len(substring) - length + 1):
            sub = substring[i:i + length]
            sub = re.sub('[^A-Za-z]', '', sub)
            if sub.lower() == sub.lower()[::-1] and len(sub) > 0:
                palindromes.add(sub)
    return palindromes