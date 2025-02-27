import re

def palindromes_between_indices(text):
    letters = sorted(re.findall('[a-zA-Z]', text[5:7]))
    if len(letters) < 3:
        return set()
    result = set()
    for i in range(len(letters) - 2):
        for j in range(i + 1, len(letters) - 1):
            for k in range(j + 1, len(letters)):
                substring = letters[i] + letters[j] + letters[k]
                if substring == substring[::-1]:
                    result.add(substring.lower())
                    result.add(substring.upper())
    return result