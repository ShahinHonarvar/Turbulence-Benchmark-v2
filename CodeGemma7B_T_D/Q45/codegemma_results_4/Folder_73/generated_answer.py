from itertools import permutations

def palindromes_between_indices(txt):
    if not txt[3:7]:
        return set()
    set_palindromes = set()
    for lst in permutations(list(txt[3:7].lower())):
        set_palindromes.add(''.join(lst))
    return set_palindromes