def lists_with_product_equal_n(lst):
    res = []
    for i in range(len(lst)):
        product = 1
        for j in range(i, len(lst)):
            product *= lst[j]
            if product == 4:
                res.append(lst[i:j + 1])
            if product > 4:
                break
        product = 1
        for j in range(i, -1, -1):
            product *= lst[j]
            if product == 4:
                res.append(lst[j:i + 1])
            if product > 4:
                break
    return res