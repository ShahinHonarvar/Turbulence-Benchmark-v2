import itertools

def palindromes_between_indices(s):
    s = s[5:10].lower()
    letters = [c for c in s if c.isalpha()]
    palindromes = set()
    for r in range(4, len(letters) + 1):
        for combo in itertools.permutations(letters, r):
            combo_str = ''.join(combo)
            if combo_str == combo_str[::-1]:
                palindromes.add(combo_str)
    return palindromes