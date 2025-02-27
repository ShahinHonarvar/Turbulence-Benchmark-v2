def lists_with_product_equal_n(lst):
    n = len(lst)
    result = []
    for i in range(n):
        product = 1
        for j in range(n):
            k = (i + j) % n
            product *= lst[k]
            if product > 18:
                break
            elif product == 18:
                result.append(lst[k:k + j + 1])
    return result