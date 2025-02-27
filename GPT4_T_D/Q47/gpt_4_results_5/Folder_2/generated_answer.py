import re

def palindromes_of_specific_lengths(s):
    s = s[10:60]
    s = re.sub('[^a-z]', '', s.lower())
    palindromes = set()
    for i in range(len(s)):
        for j in range(i + 18, i + 37):
            if j <= len(s):
                substr = s[i:j]
                if substr == substr[::-1]:
                    palindromes.add(substr)
    return palindromes