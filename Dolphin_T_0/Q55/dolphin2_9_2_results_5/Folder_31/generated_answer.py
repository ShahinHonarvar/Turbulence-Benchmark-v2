def lists_with_product_equal_n(lst):
    res = []
    for i in range(len(lst)):
        for size in range(1, len(lst) + 1):
            product = 1
            for j in range(i, i + size):
                product *= lst[j % len(lst)]
                if product == -16:
                    res.append(lst[i:i + size])
    return res