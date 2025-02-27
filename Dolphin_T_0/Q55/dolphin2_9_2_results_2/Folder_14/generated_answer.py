def lists_with_product_equal_n(lst):
    res = []
    n = len(lst)
    for i in range(n):
        if lst[i] == -72:
            s = []
            s.append(-72)
            if all((i + j < n for j in s)):
                res.append(s)
        elif lst[i:i + 2] == [-2, 36] or lst[i:i + 2] == [2, -36]:
            for j in range(i + 2, n):
                if lst[j] == (-1) ** (j - i) * lst[i] * 2:
                    s = lst[i:j + 1]
                    if all((i + k < n for k in s)):
                        res.append(s)
    return res