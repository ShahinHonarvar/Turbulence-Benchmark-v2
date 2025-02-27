import re

def palindromes_of_specific_lengths(s):
    s = s[23:78]
    s = re.sub('[^A-Za-z]', '', s).lower()
    palindromes = set()
    for length in range(13, 41):
        for i in range(len(s) - length + 1):
            substring = s[i:i + length]
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes