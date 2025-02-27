def lists_with_product_equal_n(lst):
    res = []
    for i in range(len(lst)):
        product = 1
        for n in lst[i:]:
            product *= n
            if product > 72:
                break
            elif product == 72:
                res.append(lst[i:i + n])
    return res