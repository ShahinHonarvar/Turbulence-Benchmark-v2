def lists_with_product_equal_n(lst):
    n = len(lst)
    result = []
    for i in range(n):
        product = 1
        for j in range(i, n + i):
            product *= lst[j % n]
            if product == 714:
                result.append(lst[i:j % n + 1])
            elif product > 714:
                break
    return result