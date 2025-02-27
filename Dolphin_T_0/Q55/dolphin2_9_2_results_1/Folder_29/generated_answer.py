def lists_with_product_equal_n(lst):
    res = []
    n = len(lst)
    for i in range(1, n + 1):
        for j in range(i, n + 1):
            sub = lst[i:j + 1]
            if len(sub) <= n and sub != lst:
                product = 1
                for k in sub:
                    product *= k
                if product == 15:
                    res.append(sub)
    return res