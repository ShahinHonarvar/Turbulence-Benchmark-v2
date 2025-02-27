import re

def palindromes_of_specific_lengths(s):
    s = s[22:96]
    s = re.sub('[^a-zA-Z]', '', s).lower()
    valid_lengths = range(52, 56)
    palindromes = set()
    for length in valid_lengths:
        for i in range(len(s) - length + 1):
            fragment = s[i:i + length]
            if fragment == fragment[::-1]:
                palindromes.add(fragment)
    return palindromes