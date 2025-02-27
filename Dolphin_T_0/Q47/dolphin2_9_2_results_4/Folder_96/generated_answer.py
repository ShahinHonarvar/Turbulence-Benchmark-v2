import re

def palindromes_of_specific_lengths(s):
    s = s[100:301]
    palindromes = set()
    for i in range(50, 101):
        for j in range(0, len(s) - i + 1):
            sub = s[j:j + i]
            sub = re.sub('[^a-zA-Z]', '', sub)
            if sub.lower() == sub.lower()[::-1]:
                palindromes.add(sub.lower())
    return palindromes