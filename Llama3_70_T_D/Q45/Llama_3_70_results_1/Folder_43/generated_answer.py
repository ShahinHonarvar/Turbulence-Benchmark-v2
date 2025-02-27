from itertools import combinations, permutations

def palindromes_between_indices(s):
    s = s.lower()
    chars = [c for c in s[2:6] if c.isalpha()]
    palindromes = set()
    for r in range(2, len(chars) + 1):
        for combo in combinations(chars, r):
            for perm in permutations(combo):
                word = ''.join(perm)
                if word == word[::-1] and len(word) >= 4:
                    palindromes.add(word)
    return palindromes