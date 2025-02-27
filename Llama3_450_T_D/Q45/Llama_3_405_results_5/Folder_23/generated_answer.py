from collections import Counter
    from itertools import permutations

def palindromes_between_indices(s):
    s = s[:7].lower()
    letters = [c for c in s if c.isalpha()]
    letter_counts = Counter(letters)
    palindromes = set()
    for r in range(2, len(letters) // 2 + 1):
        for combo in permutations(letters, r):
            combo_str = ''.join(combo)
            if combo_str == combo_str[::-1]:
                for p in permutations(letters, r * 2):
                    p_str = ''.join(p)
                    if p_str == p_str[::-1] and combo_str in p_str:
                        palindromes.add(p_str)
    return {p for p in palindromes if len(p) >= 4}