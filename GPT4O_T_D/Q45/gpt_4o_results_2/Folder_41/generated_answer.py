from itertools import permutations

def palindromes_between_indices(s):
    if len(s) < 4:
        return set()
    chars = s[2:4]
    chars = [ch.lower() for ch in chars if ch.isalpha()]
    potential_palindromes = set()
    for perm in permutations(chars):
        if len(perm) >= 3:
            for i in range(len(perm) - 2):
                candidate = perm[i:i + 3]
                if candidate == candidate[::-1]:
                    potential_palindromes.add(''.join(candidate))
    return potential_palindromes