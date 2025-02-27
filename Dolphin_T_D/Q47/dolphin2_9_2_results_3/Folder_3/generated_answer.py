import re

def palindromes_of_specific_lengths(s):
    s = s[27:96]
    s = re.sub('[^A-Za-z]', '', s)
    palindromes = set()
    for i in range(len(s) - 48):
        for j in range(i + 49, min(i + 51, len(s)) + 1):
            sub = s[i:j]
            if sub.lower() == sub.lower()[::-1]:
                palindromes.add(sub)
    return palindromes