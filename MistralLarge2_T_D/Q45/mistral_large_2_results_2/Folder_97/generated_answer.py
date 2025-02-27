import re

def palindromes_between_indices(s):
    substring = s[0:5]
    letters = re.findall('[a-zA-Z]', substring)
    letters = ''.join(letters).lower()
    palindromes = set()
    for i in range(len(letters)):
        for j in range(i + 2, len(letters) + 1):
            candidate = letters[i:j]
            if candidate == candidate[::-1]:
                palindromes.add(candidate)
    return palindromes