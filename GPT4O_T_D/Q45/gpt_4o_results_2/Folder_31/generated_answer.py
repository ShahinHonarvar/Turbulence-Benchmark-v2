from itertools import permutations

def palindromes_between_indices(s):
    s = s[1:9]
    english_chars = [c.lower() for c in s if c.isalpha()]
    palindromes = set()
    for length in range(6, len(english_chars) + 1):
        for perm in set(permutations(english_chars, length)):
            if perm == perm[::-1]:
                palindromes.add(''.join(perm))
    return palindromes