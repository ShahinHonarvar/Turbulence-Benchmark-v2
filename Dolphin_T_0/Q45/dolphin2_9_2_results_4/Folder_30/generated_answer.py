def palindromes_between_indices(s):
    l = [c.lower() for c in s if 'a' <= c.lower() <= 'z']
    if len(l) < 2:
        return set()
    res = set()

    def dfs(i):
        if i == len(l) // 2:
            res.add(s)
        else:
            dfs(i + 1)
            for j in range(i, len(l) - i):
                l[i], l[j] = (l[j], l[i])
                dfs(i + 1)
                l[i], l[j] = (l[j], l[i])
    dfs(0)
    return res