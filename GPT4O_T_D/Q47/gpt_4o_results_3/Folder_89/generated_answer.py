import re

def palindromes_of_specific_lengths(s):
    s = s[18:89]
    s = ''.join(re.findall('[a-zA-Z]', s)).lower()
    palindromes = set()
    for length in range(12, 15):
        for i in range(len(s) - length + 1):
            substring = s[i:i + length]
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes