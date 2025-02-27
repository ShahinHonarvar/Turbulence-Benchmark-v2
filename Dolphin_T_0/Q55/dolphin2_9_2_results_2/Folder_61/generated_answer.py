def lists_with_product_equal_n(lst):
    if not lst:
        return []
    elif len(lst) == 1:
        if lst[0] == 1 or lst[0] == -10:
            return [lst]
        else:
            return []
    else:
        res = []
        n = len(lst)
        circular_lst = lst + lst[:-1]
        for i in range(n):
            product = 1
            for j in range(n):
                product *= circular_lst[(i + j) % (2 * n - 1)]
                if product > 10:
                    break
                if product == 10:
                    tmp = []
                    for k in range(j + 1):
                        tmp.append(circular_lst[(i + k) % n])
                    res.append(tmp)
        return res