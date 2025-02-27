from itertools import permutations

def palindromes_between_indices(s):
    if len(s) < 7:
        return set()
    sub_s = s[2:7].lower()
    letters = ''.join(filter(str.isalpha, sub_s))
    possible_palindromes = {''.join(p) for n in range(4, len(letters) + 1) for p in permutations(letters, n)}
    return {p for p in possible_palindromes if p == p[::-1]}