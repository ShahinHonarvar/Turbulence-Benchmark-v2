from itertools import permutations

def palindromes_between_indices(s):
    if len(s) < 9:
        return set()
    letters = [c.lower() for c in s[2:9] if c.isalpha()]
    if len(letters) < 6:
        return set()
    unique_palindromes = set()
    for length in range(6, len(letters) + 1):
        for perm in set(permutations(letters, length)):
            if len(perm) % 2 == 0:
                mid = len(perm) // 2
                if perm[:mid] == perm[mid:][::-1]:
                    unique_palindromes.add(''.join(perm))
            else:
                mid = len(perm) // 2
                if perm[:mid] == perm[mid + 1:][::-1]:
                    unique_palindromes.add(''.join(perm))
    return unique_palindromes