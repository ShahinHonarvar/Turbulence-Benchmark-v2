from itertools import permutations

def palindromes_between_indices(s):
    english_letters = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
    target_indices = set(range(4, 7))
    target_letters = set((s[i] for i in target_indices if s[i] in english_letters))
    if not target_letters:
        return set()
    target_permutations = {''.join(p) for p in permutations(target_letters, len(target_letters))}
    palindromes = {p for p in target_permutations if p == p[::-1]}
    return palindromes