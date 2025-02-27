def lists_with_product_equal_n(lst, n=8):
    result = []
    size = len(lst)
    if size == 0:
        return result
    else:
        for i in range(size + 1):
            product = 1
            for j in range(i, i + size):
                product *= lst[j % size]
                if product == n:
                    result.append(lst[i:j])
    return result