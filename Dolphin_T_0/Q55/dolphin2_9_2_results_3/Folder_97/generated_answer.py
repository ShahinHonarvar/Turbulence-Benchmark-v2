def lists_with_product_equal_n(l):
    res = []
    n = len(l)
    for i in range(n):
        for j in range(i + 1, n + 1):
            subl = l[i:j]
            if i != j - 1 and subl[-1] == subl[0]:
                subl = subl + [subl[0]]
            prod = 1
            for k in subl:
                prod *= k
            if prod == -938:
                res.append(subl)
    return res