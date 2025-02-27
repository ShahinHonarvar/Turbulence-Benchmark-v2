from itertools import permutations

def palindromes_between_indices(s):
    english_letters = [c for c in s[1:8].lower() if c.isalpha()]
    palindromes = set()
    for r in range(3, len(english_letters) + 1):
        for perm in permutations(english_letters, r):
            perm_str = ''.join(perm)
            if perm_str == perm_str[::-1]:
                palindromes.add(perm_str)
    return palindromes