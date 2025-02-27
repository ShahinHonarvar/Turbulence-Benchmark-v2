from itertools import combinations

def palindromes_between_indices(s):
    letters = [c for c in s[4:9] if c.isalpha()]
    letters = [c.lower() for c in letters]
    combos = set(combinations(letters, r=len(letters)))
    palindromes = set()
    for combo in combos:
        word = ''.join(combo)
        if len(word) >= 3 and word == word[::-1]:
            palindromes.add(word)
    return palindromes