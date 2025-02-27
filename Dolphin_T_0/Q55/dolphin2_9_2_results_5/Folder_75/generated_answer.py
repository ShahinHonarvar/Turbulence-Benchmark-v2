def lists_with_product_equal_n(lst, n=13):
    result = []
    size = len(lst)
    for i in range(size):
        product = 1
        for j in range(i, size + i):
            if product == n:
                result.append(lst[i:j + 1])
            product *= lst[j % size]
    return result