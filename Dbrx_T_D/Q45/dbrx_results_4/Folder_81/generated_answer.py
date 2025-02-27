from itertools import permutations

def palindromes_between_indices(s):
    eng_letters = frozenset('abcdefghijklmnopqrstuvwxyz')
    found_palindromes = set()
    for i in range(7):
        for j in range(i, 7):
            substr = s[i:j + 1].lower()
            if len(substr) < 3:
                continue
            substr = ''.join((c for c in substr if c in eng_letters))
            if len(substr) < 3:
                continue
            if substr == substr[::-1]:
                found_palindromes.add(substr)
    return found_palindromes