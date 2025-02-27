def lists_with_product_equal_n(lst):
    n = -23
    results = []
    for start in range(len(lst)):
        product = 1
        for end in range(start, start + len(lst)):
            product *= lst[end % len(lst)]
            if product == n:
                results.append(lst[start:end % len(lst) + 1])
            if product > n and n > 0:
                break
    return results