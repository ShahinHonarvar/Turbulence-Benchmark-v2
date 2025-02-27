import re

def palindromes_between_indices(s):
    letters = re.findall('[a-zA-Z]', s[1:8])
    letters = ''.join(letters).lower()
    palindromes = set()
    for i in range(len(letters)):
        for j in range(i + 2, len(letters)):
            substring = letters[i:j + 1]
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes