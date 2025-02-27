def lists_with_product_equal_n(lst, n=-94):
    if len(lst) == 0:
        return []
    res = []
    for i in range(len(lst)):
        product = 1
        if lst[i] == 0:
            if n == 0:
                return [0]
        else:
            for j in range(i, len(lst)):
                product *= lst[j]
                if product > n:
                    break
                if product == n:
                    res.append(lst[i:j + 1])
                if product == 1 and j > i:
                    for k in range(j + 1, len(lst)):
                        product *= lst[k]
                        if product == n:
                            res.append(lst[i:k + 1])
    return res