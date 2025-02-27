def all_even_ints_exclusive(list):
    ans = []
    for i in range(362, 643):
        if list[i] % 2 == 0:
            ans.append(list[i])
    if len(ans) == 0:
        return []
    return ans