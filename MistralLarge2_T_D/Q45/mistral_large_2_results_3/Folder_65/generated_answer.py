from itertools import permutations

def palindromes_between_indices(s):
    letters = [ch.lower() for ch in s[:7] if ch.isalpha()]
    palindromes = set()
    for length in range(5, len(letters) + 1):
        for perm in permutations(letters, length):
            if perm == perm[::-1]:
                palindromes.add(''.join(perm))
    return palindromes