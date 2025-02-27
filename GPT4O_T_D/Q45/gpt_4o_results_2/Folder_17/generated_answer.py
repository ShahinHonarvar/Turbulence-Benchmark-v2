from itertools import permutations

def palindromes_between_indices(s):
    s = s[2:7].lower()
    letters = [ch for ch in s if ch.isalpha()]
    palindromes = set()
    for length in range(4, len(letters) + 1):
        for perm in permutations(letters, length):
            if perm == perm[::-1]:
                palindromes.add(''.join(perm))
    return palindromes