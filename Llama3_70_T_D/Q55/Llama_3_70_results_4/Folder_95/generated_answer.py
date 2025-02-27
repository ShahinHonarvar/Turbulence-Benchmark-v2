def lists_with_product_equal_n(lst):
    n = len(lst)
    result = []
    for i in range(n):
        product = 1
        for j in range(n):
            idx = (i + j) % n
            product *= lst[idx]
            if product == 28:
                result.append(lst[idx - j:idx + 1] if j != 0 else [lst[idx]])
            elif product > 28:
                break
    return result