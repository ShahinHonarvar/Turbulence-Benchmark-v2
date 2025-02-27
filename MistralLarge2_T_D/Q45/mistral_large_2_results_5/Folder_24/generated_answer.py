import itertools

def palindromes_between_indices(s):
    chars = [c.lower() for c in s[2:10] if c.isalpha()]
    palindromes = set()
    for length in range(4, len(chars) + 1):
        for combo in itertools.combinations(chars, length):
            if combo == combo[::-1]:
                palindromes.add(''.join(combo))
    return palindromes