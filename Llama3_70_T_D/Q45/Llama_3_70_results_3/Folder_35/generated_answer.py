from itertools import combinations, permutations

def palindromes_between_indices(s):
    letters = [char.lower() for char in s[2:5] if char.isalpha()]
    palindromes = set()
    for r in range(4, len(letters) + 1):
        for combo in combinations(letters, r):
            for perm in permutations(combo):
                word = ''.join(perm)
                if word == word[::-1]:
                    palindromes.add(word)
    return palindromes