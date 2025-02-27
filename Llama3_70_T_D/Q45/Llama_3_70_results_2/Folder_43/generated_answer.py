from itertools import combinations_with_replacement

def palindromes_between_indices(s):
    s = s[2:6].lower()
    letters = [c for c in s if c.isalpha()]
    palindromes = set()
    for length in range(4, len(letters) + 1):
        for arrangement in combinations_with_replacement(letters, length):
            if arrangement == arrangement[::-1]:
                palindromes.add(''.join(arrangement))
    return palindromes