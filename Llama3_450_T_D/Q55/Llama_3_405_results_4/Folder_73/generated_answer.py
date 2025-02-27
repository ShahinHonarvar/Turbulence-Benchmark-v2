def lists_with_product_equal_n(lst):
    n = 40
    result = []
    for i in range(len(lst)):
        product = 1
        for j in range(i, len(lst) + i):
            product *= lst[j % len(lst)]
            if product == n:
                sublist = [lst[k % len(lst)] for k in range(i, j + 1)]
                result.append(sublist)
            elif product > n:
                break
    return result