def lists_with_product_equal_n(lst):
    res = []
    n = len(lst)
    for i in range(n):
        for j in range(i + 1, n + 1):
            if i == j:
                continue
            elif i + 1 == j:
                if lst[i] * lst[j - 1] == -1:
                    res.append(lst[i:j])
            else:
                product = 1
                for k in range(i, j):
                    product *= lst[k]
                if product == -1:
                    res.append(lst[i:j])
    return res