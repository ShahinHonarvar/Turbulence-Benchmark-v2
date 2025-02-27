def palindromes_between_indices(s):
    letters = [c for c in s[3:7] if c.lower() in 'abcdefghijklmnopqrstuvwxyz']
    res = set()
    for i in range(6, len(s[3:7]) + 1):
        for p in permutations(letters, i):
            if ''.join(p).lower() == ''.join(p[::-1]).lower():
                res.add(''.join(p))
    return res