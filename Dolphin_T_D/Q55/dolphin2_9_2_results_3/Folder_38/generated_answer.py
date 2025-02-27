def lists_with_product_equal_n(lst):
    n = len(lst)
    if n == 0:
        return []
    lst = lst + lst[:2]
    ans = []
    for i in range(n):
        for j in range(i + 2, n - 1):
            if lst[i] * lst[j] == -23:
                ans.append(lst[i:j + 1])
            for k in range(j + 2, n + 2):
                if lst[j] * lst[k] == -23:
                    ans.append(lst[j:k + 1])
    return ans