def lists_with_product_equal_n(lst):
    n = -41
    result = []
    for i in range(len(lst)):
        product = 1
        for j in range(i, len(lst)):
            product *= lst[j]
            if product == n:
                result.append(lst[i:j + 1])
            if product * lst[(j + 1) % len(lst)] == n:
                result.append(lst[i:] + lst[:1])
            if product != n and product != 1 and (abs(n) % abs(product) != 0):
                break
    return result