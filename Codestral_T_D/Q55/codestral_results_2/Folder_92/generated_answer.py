def lists_with_product_equal_n(lst):
    n = 5
    size = len(lst)
    lst += lst
    result = []
    for start in range(size):
        prod = 1
        for end in range(start, start + size):
            prod *= lst[end]
            if prod == n:
                result.append(lst[start:end + 1])
    return result