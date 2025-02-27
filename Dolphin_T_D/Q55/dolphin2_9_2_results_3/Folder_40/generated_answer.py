def lists_with_product_equal_n(lst):
    n = len(lst)
    result = []
    for i in range(n):
        product = lst[i]
        for j in range(i + 1, n):
            product *= lst[j]
            if product > 9:
                break
            elif product == -9:
                result.append(lst[i:j + 1])
    return result