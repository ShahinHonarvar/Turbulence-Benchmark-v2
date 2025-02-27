import itertools

def palindromes_between_indices(s):
    chars = [c for c in s[2:6].lower() if c.isalpha()]
    palindromes = set()
    for length in range(3, len(chars) + 1):
        for combo in itertools.combinations(chars, length):
            candidate = ''.join(combo)
            if candidate == candidate[::-1]:
                palindromes.add(candidate)
    return palindromes