def lists_with_product_equal_n(lst):
    n = -22
    result = []
    for i in range(len(lst)):
        product = 1
        sublist = []
        for j in range(i, len(lst) + i):
            product *= lst[j % len(lst)]
            sublist.append(lst[j % len(lst)])
            while product > n:
                product /= sublist.pop(0)
            if product == n:
                result.append(sublist.copy())
            if product < n:
                break
    return result