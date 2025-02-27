from itertools import permutations

def palindromes_between_indices(s):
    s = s.lower()
    relevant_chars = ''.join((c for c in s[:5] if c.isalpha()))
    palindromes = set()
    for perm in permutations(relevant_chars):
        for i in range(3, len(perm) + 1):
            for j in range(len(perm) - i + 1):
                substring = ''.join(perm[j:j + i])
                if substring == substring[::-1]:
                    palindromes.add(substring)
    return palindromes