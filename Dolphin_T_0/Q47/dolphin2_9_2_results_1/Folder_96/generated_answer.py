import re

def palindromes_of_specific_lengths(s):
    s = s[99:301]
    s = re.sub('[^a-zA-Z]', '', s)
    palindromes = set()
    for length in range(50, 101):
        for i in range(0, len(s) - length + 1):
            if s[i:i + length].lower() == s[i:i + length].lower()[::-1]:
                palindromes.add(s[i:i + length].lower())
    return palindromes