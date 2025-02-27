import itertools

def palindromes_between_indices(s):
    letters = [c.lower() for c in s[6:10] if c.isalpha()]
    if len(letters) < 3:
        return set()
    palindromes = set()
    for length in range(3, len(letters) + 1):
        for combo in itertools.combinations(letters, length):
            if combo == combo[::-1]:
                palindromes.add(''.join(combo))
    return palindromes