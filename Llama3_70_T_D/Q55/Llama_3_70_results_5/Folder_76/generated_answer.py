def lists_with_product_equal_n(lst):
    if not lst:
        return []
    n = len(lst)
    result = []
    for i in range(n):
        product = 1
        for j in range(i, i + n):
            product *= lst[j % n]
            if product == 247:
                result.append(lst[i % n:j % n + 1])
            elif product > 247:
                break
    return result