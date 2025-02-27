def lists_with_product_equal_n(lst):
    result = []
    size = len(lst)
    for i in range(size):
        product = 1
        for j in range(i, size + i):
            product *= lst[j % size]
            if product == 851:
                tmp = []
                for k in range(i, j + 1):
                    tmp.append(lst[k % size])
                result.append(tmp)
    return result