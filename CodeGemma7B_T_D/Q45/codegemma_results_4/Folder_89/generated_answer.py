from itertools import permutations
    from itertools import permutations

def palindromes_between_indices(s):
    if len(s) < 6:
        return set()
    english_letters = 'abcdefghijklmnopqrstuvwxyz'
    letters_between_indices = s[5:10].lower()
    return {''.join(p) for p in permutations(sorted(letters_between_indices)) if ' '.join(p).isalpha()}