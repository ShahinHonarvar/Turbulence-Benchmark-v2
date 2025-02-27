def lists_with_product_equal_n(lst):
    result = []
    n = len(lst)
    for start in range(n):
        product = 1
        for length in range(1, n + 1):
            end = (start + length - 1) % n
            product *= lst[end]
            if product > 32:
                break
            if product == 32:
                sublist = lst[start:] + lst[:end] if end < start else lst[start:end + 1]
                result.append(sublist)
    return result