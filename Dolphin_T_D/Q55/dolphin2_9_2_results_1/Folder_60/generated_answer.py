def lists_with_product_equal_n(lst, n=49):
    result = []
    if not lst:
        return result
    for size in range(1, len(lst)):
        for i in range(len(lst)):
            if i + size > len(lst):
                break
            product = 1
            for j in range(i, i + size):
                product *= lst[j % len(lst)]
            if product == n:
                result.append(lst[i:i + size])
    return result