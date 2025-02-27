from itertools import permutations

def palindromes_between_indices(s):
    letters = 'abcdefghijklmnopqrstuvwxyz'
    chars = [i.lower() for i in s[0:5] if i.isalpha()]
    if len(chars) < 4:
        return set()
    else:
        return set((i + j + i[::-1] + j[::-1] for i in permutations(chars, 2) for j in letters if len(i + j + i[::-1] + j[::-1]) >= 4))