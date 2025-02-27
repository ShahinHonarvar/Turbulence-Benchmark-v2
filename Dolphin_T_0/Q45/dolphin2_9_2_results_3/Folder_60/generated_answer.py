def palindromes_between_indices(s):
    letters = set(s[3:7].lower())
    result = set()
    for i in range(4, len(s[3:7]) + 1):
        for p in permutations(letters, i):
            if ''.join(p).lower() == ''.join(reversed(p)).lower():
                result.add(''.join(p))
    return result