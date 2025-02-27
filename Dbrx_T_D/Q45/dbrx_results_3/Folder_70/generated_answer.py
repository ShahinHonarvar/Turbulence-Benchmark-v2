import re

def palindromes_between_indices(s):
    s = s[1:7].lower()
    letters = set(s)
    palindromes = set()
    if len(letters) < 2:
        return palindromes
    for letter in letters:
        for i in range(4, 7):
            pattern = re.compile(f'^[{letter}]{{2}}[^{letter}]?[{letter}]{{2}}$|^[{letter}]{{3}}[{letter}]*[{letter}]{{3}}$')
            if pattern.search(s) and len(s) >= i:
                palindromes.add(s[:i])
    return palindromes