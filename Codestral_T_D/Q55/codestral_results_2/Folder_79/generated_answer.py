def lists_with_product_equal_n(lst):
    n = len(lst)
    lst += lst
    result = []
    for i in range(n):
        product = 1
        for j in range(i, i + n):
            product *= lst[j]
            if product == -83:
                result.append(lst[i:j + 1])
            if product == 0:
                break
    return result