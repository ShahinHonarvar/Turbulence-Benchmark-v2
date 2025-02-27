def lists_with_product_equal_n(lst):
    sublists = []
    n = len(lst)
    for i in range(n):
        for j in range(i + 1, n + 1):
            sub = lst[i:j]
            if sub[-1] == sub[0]:
                prod = 1
                for k in sub:
                    prod *= k
                if prod == -76:
                    sublists.append(sub)
    return sublists