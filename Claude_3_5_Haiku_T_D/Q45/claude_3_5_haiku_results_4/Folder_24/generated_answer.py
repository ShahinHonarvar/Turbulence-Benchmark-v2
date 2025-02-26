from itertools import permutations

def palindromes_between_indices(s):
    letters = [c.lower() for c in s[2:10] if c.isalpha()]
    if len(letters) < 4:
        return set()
    unique_palindromes = set()
    for length in range(4, len(letters) + 1):
        for perm in set(permutations(letters, length)):
            sorted_perm = sorted(perm)
            for i in range(len(sorted_perm) // 2):
                if sorted_perm[i] != sorted_perm[-(i + 1)]:
                    break
            else:
                unique_palindromes.add(''.join(sorted_perm))
    return unique_palindromes