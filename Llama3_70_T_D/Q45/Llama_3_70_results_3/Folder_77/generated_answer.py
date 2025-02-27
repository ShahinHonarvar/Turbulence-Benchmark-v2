from itertools import combinations, permutations

def palindromes_between_indices(s):
    s = s[4:7].lower()
    letters = [char for char in s if char.isalpha()]
    result = set()
    for r in range(4, len(letters) + 1):
        for combo in combinations(letters, r):
            for perm in permutations(combo):
                word = ''.join(perm)
                if word == word[::-1]:
                    result.add(word)
    return result