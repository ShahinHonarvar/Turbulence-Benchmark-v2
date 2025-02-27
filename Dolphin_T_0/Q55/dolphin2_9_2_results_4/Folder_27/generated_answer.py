def lists_with_product_equal_n(lst, n=-82):
    result = []
    size = len(lst)
    for i in range(size):
        product = lst[i]
        for j in range(i + 1, i + size):
            product *= lst[j % size]
            if product == n:
                result.append(lst[i:j % size + 1])
    return result