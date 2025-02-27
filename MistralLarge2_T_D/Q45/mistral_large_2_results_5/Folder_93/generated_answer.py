import itertools

def palindromes_between_indices(s):
    relevant_chars = [c.lower() for c in s[2:8] if c.isalpha()]
    all_combinations = set((''.join(p) for r in range(6, len(relevant_chars) + 1) for p in itertools.permutations(relevant_chars, r)))
    palindromes = {comb for comb in all_combinations if comb == comb[::-1] and len(comb) >= 6}
    return palindromes