def lists_with_product_equal_n(l):
    n = len(l)
    result = []
    for i in range(n):
        product = 1
        for j in range(i, n):
            product *= l[j]
            if product == 5:
                result.append(l[i:j + 1])
            elif product > 5:
                break
    return result