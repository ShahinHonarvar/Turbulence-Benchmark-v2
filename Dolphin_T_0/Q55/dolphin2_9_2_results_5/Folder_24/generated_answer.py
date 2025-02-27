def lists_with_product_equal_n(lst, n=-89):
    size = len(lst)
    if size == 0:
        return []
    result = []
    product = 1
    for start in range(size):
        product = lst[start]
        if product == n:
            result.append([n])
        for end in range(start + 1, start + size + 1):
            product *= lst[end % size]
            if product == n:
                result.append(lst[start:start + end - start + 1])
    return result