from itertools import permutations

def palindromes_between_indices(s):
    s = s[1:7].lower()
    chars = [ch for ch in s if ch.isalpha()]
    palindromes = set()
    for combo in permutations(chars, len(chars)):
        if combo == combo[::-1]:
            palindromes.add(''.join(combo))
    return set((p for p in palindromes if len(p) >= 6))