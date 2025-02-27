import re

def palindromes_of_specific_lengths(s):
    candidates = set()
    s = s[30:85].lower()
    for start in range(len(s)):
        for end in range(start + 12, start + 21):
            if end <= len(s):
                substring = s[start:end]
                if re.match('^[a-z]*$', substring) and substring == substring[::-1]:
                    candidates.add(substring)
    return candidates