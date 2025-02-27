from itertools import combinations, permutations
from string import ascii_lowercase

def palindromes_between_indices(s):
    letters = [c for i, c in enumerate(s) if i >= 5 and i <= 6 and (c.lower() in ascii_lowercase)]
    letters = [c.lower() for c in letters]
    result = set()
    for r in range(3, len(letters) + 1):
        for combo in combinations(letters, r):
            for perm in permutations(combo):
                middle_index = len(perm) // 2
                left = ''.join(perm[:middle_index])
                right = ''.join(perm[middle_index:])[::-1]
                if left == right:
                    result.add(''.join(perm))
    return result