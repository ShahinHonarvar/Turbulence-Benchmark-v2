def palindromes_between_indices(s):
    chars = [c.lower() for c in s[:5] if c.isalpha()]
    result = set()
    for i in range(3, len(chars) + 1):
        for j in combinations(chars, i):
            for p in permutations(j):
                if ''.join(p).lower() == ''.join(p[::-1]).lower():
                    result.add(''.join(p))
    return result