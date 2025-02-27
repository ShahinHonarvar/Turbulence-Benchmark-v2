import re

def palindromes_between_indices(s):
    alphabets = []
    for c in s[2:8]:
        if re.match('[a-z]', c) or re.match('[A-Z]', c):
            alphabets.append(c.lower())
    length = len(alphabets)
    result = set([])
    for i in range(length):
        for j in range(i + 2, length + 1):
            sub = ''.join(alphabets[i:j])
            if len(sub) >= 3 and sub == sub[::-1]:
                result.add(sub)
    return result