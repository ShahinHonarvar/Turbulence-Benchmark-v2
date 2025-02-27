import re

def palindromes_between_indices(s):
    letters = re.findall('[a-zA-Z]', s[1:9])
    letters = ''.join(letters).lower()
    palindromes = set()
    n = len(letters)
    for length in range(4, n + 1):
        for i in range(n - length + 1):
            substring = letters[i:i + length]
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes