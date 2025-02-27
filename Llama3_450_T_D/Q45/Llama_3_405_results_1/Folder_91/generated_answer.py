import itertools

def palindromes_between_indices(s):
    letters = [char.lower() for char in s[2:7] if char.isalpha()]
    if len(letters) < 3:
        return set()
    palindromes = set()
    for r in range(3, len(letters) + 1):
        for combo in itertools.permutations(letters, r):
            combo_str = ''.join(combo)
            if combo_str == combo_str[::-1]:
                palindromes.add(combo_str)
    return palindromes