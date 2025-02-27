from itertools import combinations, permutations

def palindromes_between_indices(s):
    s = s[3:10].lower()
    letters = [c for c in s if c.isalpha()]
    palindromes = set()
    for r in range(3, len(letters) + 1):
        for combo in combinations(letters, r):
            if combo.count(combo[0]) > 1 and len(combo) % 2 == 1:
                for perm in permutations(combo):
                    word = ''.join(perm)
                    if word == word[::-1]:
                        palindromes.add(word)
            elif len(combo) % 2 == 0:
                for perm in permutations(combo):
                    word = ''.join(perm)
                    if word == word[::-1]:
                        palindromes.add(word)
    return palindromes