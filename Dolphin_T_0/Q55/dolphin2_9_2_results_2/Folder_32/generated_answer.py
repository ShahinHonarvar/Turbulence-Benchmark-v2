def lists_with_product_equal_n(lst, n=76):
    if len(lst) == 0:
        return []
    result = []
    product = 1
    for start in range(len(lst)):
        product = 1
        for end in range(start, len(lst) + start):
            product *= lst[end % len(lst)]
            if product == n:
                result.append(lst[start:end + 1])
            elif product > n:
                break
    return result