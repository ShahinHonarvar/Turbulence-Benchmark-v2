import re

def palindromes_of_specific_lengths(s):
    s = s[124:284]
    pattern = re.compile('[A-Za-z]')
    s = re.findall(pattern, s)
    s = ''.join(s.lower())
    palindromes = set()
    for length in range(115, 135):
        for i in range(len(s) - length + 1):
            if s[i:i + length] == s[i:i + length][::-1]:
                palindromes.add(s[i:i + length])
    return palindromes