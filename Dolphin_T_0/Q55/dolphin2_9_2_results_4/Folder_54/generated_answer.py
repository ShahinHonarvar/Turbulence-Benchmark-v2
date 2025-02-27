def lists_with_product_equal_n(lst):
    result = []
    n = -17
    size = len(lst)
    for i in range(size):
        product = 1
        for j in range(i, i + size):
            product *= lst[j % size]
            if product == n:
                result.append(lst[i:j + 1])
    return result