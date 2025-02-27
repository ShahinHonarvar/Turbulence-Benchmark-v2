from itertools import permutations, combinations

def palindromes_between_indices(s):
    s = s[4:10].lower()
    letters = [i for i in s if i.isalpha()]
    if not letters:
        return set()
    palindromes = set()
    for r in range(4, len(letters) + 1):
        for p in set(permutations(letters, r)):
            if p == p[::-1]:
                palindromes.add(''.join(p))
    return palindromes