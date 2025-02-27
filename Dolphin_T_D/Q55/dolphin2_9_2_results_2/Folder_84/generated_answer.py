def lists_with_product_equal_n(lst, n=-906):
    result = []
    for i in range(len(lst)):
        product = 1
        start = i
        for end in range(i, len(lst)):
            product *= lst[end]
            if product > n:
                break
            elif product == n:
                result.append(lst[start:end + 1])
    return result