from itertools import permutations

def palindromes_between_indices(s):
    substr = s[6:10].lower()
    letters = [ch for ch in substr if ch.isalpha()]
    palindromes = set()
    for perm in permutations(letters):
        for size in range(3, len(perm) + 1):
            for start in range(len(perm) - size + 1):
                candidate = perm[start:start + size]
                if candidate == candidate[::-1]:
                    palindromes.add(''.join(candidate))
    return palindromes