import re

def palindromes_of_specific_lengths(s):
    substring = re.sub('[^a-zA-Z]', '', s[34:91]).lower()
    palindromes = set()
    for length in range(14, 40):
        for i in range(len(substring) - length + 1):
            candidate = substring[i:i + length]
            if candidate == candidate[::-1]:
                palindromes.add(s[34:91][i:i + length])
    return palindromes