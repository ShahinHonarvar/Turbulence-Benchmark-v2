import itertools

def palindromes_between_indices(s):
    letters = [c for c in s[2:6] if c.isalpha()]
    letters = [c.lower() for c in letters]
    palindromes = set()
    for length in range(4, len(letters) + 1):
        for combo in itertools.combinations_with_replacement(letters, length):
            if combo == combo[::-1]:
                palindromes.add(''.join(combo))
    return palindromes