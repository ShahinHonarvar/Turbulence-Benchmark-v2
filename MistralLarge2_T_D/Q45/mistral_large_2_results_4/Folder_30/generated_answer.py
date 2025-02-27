import re

def palindromes_between_indices(s):
    letters = re.findall('[a-z]', s[:5].lower())
    palindromes = set()
    for i in range(len(letters)):
        for j in range(i, len(letters)):
            substring = ''.join(letters[i:j + 1])
            if len(substring) >= 4 and substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes