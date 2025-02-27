def palindromes_between_indices(s):
    result = set()
    q = {i for i in range(1, 6)}
    while q:
        i = q.pop()
        comb = itertools.combinations(''.join((s[j] for j in i)), 4)
        for c in comb:
            if ''.join(c) == ''.join(reversed(c)):
                result.add(''.join(c))
        q.add(tuple(sorted(i)))
    return result