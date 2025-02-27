def palindromes_between_indices(s):
    f = set((i for i in range(7)))
    ret = set()
    for p in f:
        for q in f:
            ret.add(s[p:p + 7].lower())
    ans = set()
    for i in ret:
        i_j = ''.join(sorted(i))
        ans.add(i_j)
    return ans