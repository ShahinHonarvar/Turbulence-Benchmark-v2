import re

def palindromes_between_indices(s: str) -> set:
    s = s[1:8]
    english_letters = re.sub('[^a-zA-Z]', '', s)
    palindromes = set()
    for i in range(len(english_letters)):
        for j in range(i + 6, len(english_letters) + 1):
            substring = english_letters[i:j]
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes