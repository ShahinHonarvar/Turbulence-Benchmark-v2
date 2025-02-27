from itertools import permutations

def palindromes_between_indices(s):
    if len(s) < 10:
        return set()
    sub_str = s[6:10].lower()
    english_letters = [ch for ch in sub_str if ch.isalpha()]
    palindromes_set = set()
    for perm in permutations(english_letters):
        perm_str = ''.join(perm)
        if len(perm_str) >= 5 and perm_str == perm_str[::-1]:
            palindromes_set.add(perm_str)
    return palindromes_set