def lists_with_product_equal_n(lst):
    n = len(lst)
    res = []
    for i in range(n):
        product = 1
        for j in range(i, i + n):
            if j == n:
                if product == -75:
                    sublist = lst[i:] + lst[:i]
                    res.append(sublist)
                break
            product *= lst[j % n]
            if product == -75:
                sublist = lst[i:j + 1]
                res.append(sublist)
    return res