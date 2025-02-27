from itertools import permutations

def palindromes_between_indices(s):
    s = s.lower()
    relevant_part = [c for c in s[4:7] if c.isalpha()]
    palindromes = set()
    if len(relevant_part) < 4:
        return set()
    for length in range(4, len(relevant_part) + 1):
        for perm in permutations(relevant_part, length):
            if perm == perm[::-1]:
                palindromes.add(''.join(perm))
    return palindromes