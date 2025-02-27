from itertools import permutations

def palindromes_between_indices(s):
    letters = [ch for ch in s[:8].lower() if ch.isalpha()]
    palindromes = set()
    for length in range(6, len(letters) + 1):
        for perm in permutations(letters, length):
            if perm == perm[::-1]:
                palindromes.add(''.join(perm))
    return palindromes