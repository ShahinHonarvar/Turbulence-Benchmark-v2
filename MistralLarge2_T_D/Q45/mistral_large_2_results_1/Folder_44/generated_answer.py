import itertools

def palindromes_between_indices(s):
    letters = [c for c in s[2:8] if c.isalpha()]
    letters = [c.lower() for c in letters]
    palindromes = set()
    for length in range(3, len(letters) + 1):
        for combo in itertools.permutations(letters, length):
            if combo == combo[::-1]:
                palindromes.add(''.join(combo))
    return palindromes