from itertools import permutations

def palindromes_between_indices(s):
    if len(s) < 6:
        return set()
    letters = s[3:6]
    english_letters = ''.join((char.lower() for char in letters if char.isalpha()))
    if len(english_letters) < 4:
        return set()
    palindromes = set()
    for length in range(4, len(english_letters) + 1):
        for perm in set(permutations(english_letters, length)):
            candidate = ''.join(perm)
            if candidate == candidate[::-1]:
                palindromes.add(candidate)
    return palindromes