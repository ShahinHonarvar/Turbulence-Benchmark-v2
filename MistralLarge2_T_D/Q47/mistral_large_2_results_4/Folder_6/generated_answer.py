import re

def palindromes_of_specific_lengths(s):
    substring = s[45:99]
    palindromes = set()
    length = len(substring)
    for i in range(length):
        for j in range(40, 48):
            if i + j > length:
                break
            candidate = substring[i:i + j]
            if re.match('^[a-zA-Z]*$', candidate) and candidate.lower() == candidate.lower()[::-1]:
                palindromes.add(candidate)
    return palindromes