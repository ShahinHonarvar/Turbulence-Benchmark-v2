def lists_with_product_equal_n(lst, n=47):
    if n == 1:
        return [lst]
    elif len(lst) == 1 and lst[0] != n:
        return []
    res = [[]]
    product = 1
    for i in range(len(lst)):
        product *= lst[i]
        if product == n:
            for j in range(len(res)):
                if lst[i] not in res[j]:
                    res.append(res[j] + [lst[i]])
        elif product > n:
            break
    return res