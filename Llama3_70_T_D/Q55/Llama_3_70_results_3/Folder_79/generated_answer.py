def lists_with_product_equal_n(lst):
    n = len(lst)
    result = []
    for i in range(n):
        product = 1
        for j in range(n):
            product *= lst[(i + j) % n]
            if product == -83:
                result.append(lst[i:i + j + 1])
                break
            if 0 in lst[i:i + j + 1] and len(lst[i:i + j + 1]) > 1:
                break
    return result