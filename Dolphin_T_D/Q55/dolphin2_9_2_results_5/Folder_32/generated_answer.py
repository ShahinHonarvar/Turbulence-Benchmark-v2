def lists_with_product_equal_n(lst):
    data = []
    n = len(lst)
    for i in range(n):
        product = 1
        for j in range(i, n):
            product *= lst[j]
            if product > 76:
                break
            if product == 76 and len(lst[i:j + 1]) > 1:
                data.append(lst[i:j + 1])
    return data