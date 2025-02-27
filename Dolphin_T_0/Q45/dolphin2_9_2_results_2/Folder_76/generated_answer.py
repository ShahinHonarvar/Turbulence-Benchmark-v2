def palindromes_between_indices(s):
    s = ''.join(filter(lambda x: x.lower() in 'abcdefghijklmnopqrstuvwxyz', s))
    if len(s) < 4:
        return set()
    s = s[:5]
    return {''.join(k) for i in range(len(s)) for k in itertools.combinations(s, i) if ''.join(k).lower() == ''.join(k).lower()[::-1]}