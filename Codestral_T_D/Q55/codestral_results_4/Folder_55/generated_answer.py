def lists_with_product_equal_n(lst):
    n = -6
    res = []
    for i in range(len(lst)):
        if lst[i] == n:
            res.append([lst[i]])
        elif lst[i] != 0:
            prod = lst[i]
            sub = [lst[i]]
            for j in range(i + 1, i + len(lst)):
                prod *= lst[j % len(lst)]
                sub.append(lst[j % len(lst)])
                if prod == n:
                    res.append(sub)
                elif prod != n and abs(prod) < abs(n):
                    break
    return res