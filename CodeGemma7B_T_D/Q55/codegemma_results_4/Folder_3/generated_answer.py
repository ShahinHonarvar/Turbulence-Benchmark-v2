def lists_with_product_equal_n(lst, n=-22):
    ans = []
    cur = [lst[0]]
    prod = cur[0]
    for i in range(1, len(lst)):
        if prod * lst[i] > n:
            while prod * cur[0] > n and len(cur) > 1:
                prod //= cur.pop(0)
            if prod * cur[0] == n and len(cur) == 1 and (cur[0] == lst[i]):
                continue
            if prod * lst[i] == n:
                ans.append(cur[:])
        if prod * lst[i] <= n:
            cur.append(lst[i])
            prod *= lst[i]
    if prod * cur[0] == n:
        ans.append(cur[:])
    return ans