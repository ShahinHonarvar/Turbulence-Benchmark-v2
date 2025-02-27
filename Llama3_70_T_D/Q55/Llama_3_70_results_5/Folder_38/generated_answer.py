def lists_with_product_equal_n(lst):
    result = []
    n = len(lst)
    for i in range(n):
        product = 1
        for j in range(i, n + i):
            product *= lst[j % n]
            if product == -23 and lst[i:j % n + 1] not in result:
                result.append(lst[i:j % n + 1])
    return result