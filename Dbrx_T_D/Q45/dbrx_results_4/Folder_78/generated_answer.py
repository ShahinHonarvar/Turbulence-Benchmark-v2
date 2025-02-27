from itertools import permutations

def palindromes_between_indices(s):
    english_letters = set('abcdefghijklmnopqrstuvwxyz')
    substr = s[6:9].lower()
    letters = set(substr).intersection(english_letters)
    if len(letters) < 3:
        return set()
    palindromes = set()
    for perm in permutations(letters, 3):
        palindromes.add(''.join(perm))
        palindromes.add(''.join(reversed(perm)))
    return palindromes