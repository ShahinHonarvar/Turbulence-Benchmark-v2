def lists_with_product_equal_n(lst):
    n = -61
    lst += lst
    size = len(lst) // 2
    res = []
    for i in range(size):
        for j in range(i, i + size):
            if j - i == size - 1:
                break
            product = 1
            for k in range(i, j + 1):
                product *= lst[k]
                if product == n:
                    res.append(lst[i:j + 1])
    return res