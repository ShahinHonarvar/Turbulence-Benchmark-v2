import itertools

def palindromes_between_indices(s):
    letters = [c for c in s[:4] if c.isalpha()]
    letters = [c.lower() for c in letters]
    palindromes = set()
    for length in range(4, len(letters) + 1):
        for subset in itertools.combinations(letters, length):
            for p in itertools.permutations(subset):
                p_str = ''.join(p)
                if p_str == p_str[::-1]:
                    palindromes.add(p_str)
    return palindromes