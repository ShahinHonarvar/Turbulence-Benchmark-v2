def lists_with_product_equal_n(lst):
    result = []
    n = -23
    for i in range(len(lst)):
        product = 1
        temp = []
        for j in range(i, len(lst) + i):
            product *= lst[j % len(lst)]
            temp.append(lst[j % len(lst)])
            if product == n:
                result.append(temp.copy())
            if product >= n:
                product /= lst[j - i]
                temp.pop(0)
    return result