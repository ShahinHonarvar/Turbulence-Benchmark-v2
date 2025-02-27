from itertools import permutations

def palindromes_between_indices(s):
    letters = [c.lower() for c in s[6:10] if c.isalpha()]
    palindromes = set()
    for perm in permutations(letters):
        for i in range(len(perm)):
            for j in range(i + 5, len(perm) + 1):
                if perm[i:j] == perm[i:j][::-1]:
                    palindromes.add(''.join(perm[i:j]))
    return palindromes