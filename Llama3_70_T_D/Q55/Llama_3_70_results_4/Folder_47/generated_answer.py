def lists_with_product_equal_n(lst):
    n = len(lst)
    result = []
    for i in range(n):
        product = 1
        for j in range(n):
            product *= lst[(i + j) % n]
            if product == -94:
                result.append(lst[(i + j) % n])
            if product > -94:
                break
    result2 = []
    for sublst in result:
        if len(sublst) > 1:
            result2.append(sublst)
    return result2