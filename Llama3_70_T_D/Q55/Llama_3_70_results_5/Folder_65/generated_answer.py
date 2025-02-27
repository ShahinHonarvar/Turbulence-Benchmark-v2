def lists_with_product_equal_n(lst):
    result = []
    n = len(lst)
    for i in range(n):
        product = 1
        for j in range(n):
            product *= lst[(i + j) % n]
            if product == 46:
                result.append(lst[(i + j) % n:])
                break
            elif product > 46:
                break
    return result