def palindromes_between_indices(s):
    if len(s) < 9:
        return set()
    letters = set(s[7:9].lower())
    palindromes = set()
    for i in range(3, len(s[7:9] + 1)):
        for p in permutations(letters, i):
            if ''.join(p).lower() == ''.join(p[::-1]).lower():
                palindromes.add(''.join(p))
    return palindromes