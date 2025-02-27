import re

def palindromes_of_specific_lengths(s):
    substring = s[101:293]
    substring = re.sub('[^a-zA-Z]', '', substring.lower())
    palindromes = set()
    for length in range(154, 183):
        for i in range(len(substring) - length + 1):
            candidate = substring[i:i + length]
            if candidate == candidate[::-1]:
                palindromes.add(candidate)
    return palindromes