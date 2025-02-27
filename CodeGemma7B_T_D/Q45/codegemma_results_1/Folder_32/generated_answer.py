from itertools import permutations

def palindromes_between_indices(txt):
    english_letters = 'abcdefghijklmnopqrstuvwxyz'
    palindromes = set()
    for perm in permutations(txt[1:8], 5):
        if perm[0] in english_letters and perm[-1] in english_letters:
            palindromes.add(''.join(perm))
    return palindromes