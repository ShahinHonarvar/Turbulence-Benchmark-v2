def lists_with_product_equal_n(lst):
    result = []
    size = len(lst)
    for i in range(size):
        product = 1
        for j in range(i, size + i):
            product *= lst[j % size]
            if product == -75 and [lst[j % size] for j in range(i, size + i)] not in result:
                result.append([lst[j % size] for j in range(i, size + i)])
    return result