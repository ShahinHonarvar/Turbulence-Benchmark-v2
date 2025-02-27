import re

def palindromes_between_indices(s):
    letters = re.findall('[a-zA-Z]', s[2:9])
    letters = ''.join(letters).lower()
    palindromes = set()
    for i in range(len(letters)):
        for j in range(i + 7, len(letters) + 1):
            substring = letters[i:j]
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes