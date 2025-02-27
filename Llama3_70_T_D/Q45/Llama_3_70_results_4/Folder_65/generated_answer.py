from itertools import permutations, combinations

def palindromes_between_indices(s):
    s = s[:7].lower()
    letters = [c for c in s if c.isalpha()]
    palindromes = set()
    for r in range(5, len(letters) + 1):
        for combo in combinations(letters, r):
            for perm in permutations(combo):
                word1 = ''.join(perm)
                word2 = word1[::-1]
                if word1 == word2 and word1 not in palindromes:
                    palindromes.add(word1)
    return palindromes