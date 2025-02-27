from itertools import permutations

def palindromes_between_indices(s):
    letters = [c for c in s[3:9] if c.isalpha()]
    letters = [c.lower() for c in letters]
    combos = set(permutations(letters, len(letters)))
    palindromes = set((''.join(combo) for combo in combos if ''.join(combo) == ''.join(reversed(combo)) and len(combo) >= 6))
    return palindromes