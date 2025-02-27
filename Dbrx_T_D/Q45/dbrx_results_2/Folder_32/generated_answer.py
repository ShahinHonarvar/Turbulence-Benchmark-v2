from collections import defaultdict

def palindromes_between_indices(s):
    english_letters = set('abcdefghijklmnopqrstuvwxyz')
    substr = s[1:8].lower()
    possible_letters = set(substr) & english_letters
    if len(possible_letters) < 5:
        return set()
    palindromes = set()
    for i in range(5, len(possible_letters) + 1):
        for comb in combinations(possible_letters, i):
            comb = ''.join(comb)
            if comb == comb[::-1]:
                palindromes.add(comb)
    return palindromes