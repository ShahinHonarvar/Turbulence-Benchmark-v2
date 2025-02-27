from itertools import permutations

def palindromes_between_indices(string):
    string = string.lower()[:3]
    palindromes = {''.join(p): 6 - len(''.join(p)) for p in permutations(string)}
    palindromes = {p: v for p, v in palindromes.items() if len(p) >= 3 and p == p[::-1]}
    return set(palindromes.keys())