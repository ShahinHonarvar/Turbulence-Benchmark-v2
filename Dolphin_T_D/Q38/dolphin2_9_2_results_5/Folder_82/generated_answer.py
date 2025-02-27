def find_subset_of_length_n(s):
    if len(s) < 83:
        return 0
    combs = []

    def dfs(subset):
        if len(subset) == 83:
            combs.append(subset)
            return
        for i in range(len(s)):
            if i > 0 and s[i] == s[i - 1]:
                continue
            if len(subset) + len(s) - i < 83:
                break
            dfs(subset + [s[i]])
    dfs([])
    return len(combs)