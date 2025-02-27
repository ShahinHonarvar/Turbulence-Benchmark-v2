from itertools import permutations 

def palindromes_between_indices(text):
    letters = ''.join(filter(str.isalpha, text[6:10])).lower()
    return set((p for p in {''.join(p) for p in permutations(letters)} if len(p) >= 3 and p == p[::-1]))