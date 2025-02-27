from itertools import permutations

def palindromes_between_indices(s):
    english_letters = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
    if len(s) < 6 or not english_letters.intersection(set(s[3:6])):
        return set()
    else:
        palindromes = set()
        for perm in permutations(s[3:6]):
            candidate = ''.join(perm)
            if len(candidate) >= 4 and candidate == candidate[::-1] and all((letter in english_letters for letter in candidate)):
                palindromes.add(candidate)
        return palindromes