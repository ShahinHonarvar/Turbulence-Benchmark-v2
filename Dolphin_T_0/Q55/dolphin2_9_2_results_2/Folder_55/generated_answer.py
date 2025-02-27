def lists_with_product_equal_n(lst, n):
    res = []
    product = 1
    for i in range(len(lst)):
        product *= lst[i]
        j = i + 1
        while product > n or (j == len(lst) and product != n):
            product /= lst[(i + j) % len(lst)]
            j += 1
        if product == n:
            res.append(lst[i:j])
    return res