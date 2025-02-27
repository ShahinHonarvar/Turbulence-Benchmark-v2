def lists_with_product_equal_n(lst):
    counter = lst.copy()
    res = []
    n = 1
    for i in range(len(lst)):
        product = 1
        for j in range(i, len(lst)):
            product *= counter.pop(0)
            if product % 6 == 0:
                res.append(lst[i:j + 1])
    return res