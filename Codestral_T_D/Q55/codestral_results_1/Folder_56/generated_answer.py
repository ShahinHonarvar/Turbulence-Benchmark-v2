def lists_with_product_equal_n(lst):
    n = -65
    size = len(lst)
    lst += lst
    result = []
    for i in range(size):
        product = 1
        for j in range(i, i + size):
            product *= lst[j]
            if product == n:
                result.append(lst[i:j + 1])
            if product > n:
                break
    return result