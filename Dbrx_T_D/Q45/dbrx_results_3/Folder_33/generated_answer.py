from collections import defaultdict

def palindromes_between_indices(s):
    if len(s) < 10:
        return set()
    english_letters = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
    candidates = defaultdict(set)
    for i in range(7, 10):
        for j in range(i, 10):
            for char in s[i:j + 1]:
                if char in english_letters:
                    candidates[i, j].add(char.lower())
    palindromes = set()
    for candidate in candidates.values():
        if len(candidate) >= 4:
            palindromes.add(''.join(candidate) + ''.join(reversed(candidate)))
    return palindromes