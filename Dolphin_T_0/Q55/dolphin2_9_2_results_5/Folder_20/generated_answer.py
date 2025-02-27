def lists_with_product_equal_n(lst):
    size = len(lst)
    if size < 2:
        return []
    result = []
    for i in range(size):
        product = 1
        for j in range(i, size):
            product *= lst[j]
            if product == -69:
                result.append(lst[i:j + 1])
            for k in range(j + 1, size + i):
                product *= lst[k % size]
                if product == -69:
                    result.append(lst[i:k % size] + lst[k % size])
    return result