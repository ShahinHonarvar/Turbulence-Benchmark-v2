import re

def palindromes_between_indices(s):
    letters = re.findall('[a-zA-Z]', s[1:7])
    letters = ''.join(letters).lower()
    palindromes = set()
    for length in range(3, len(letters) + 1):
        for i in range(len(letters) - length + 1):
            substring = letters[i:i + length]
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes