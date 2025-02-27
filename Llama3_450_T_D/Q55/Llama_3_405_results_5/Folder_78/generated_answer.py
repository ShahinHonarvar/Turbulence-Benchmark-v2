def lists_with_product_equal_n(lst):
    n = len(lst)
    result = []
    for i in range(n):
        product = 1
        for j in range(i, i + n):
            product *= lst[j % n]
            if product == 74:
                result.append([lst[k % n] for k in range(i, j + 1)])
            elif product > 74:
                break
    return result