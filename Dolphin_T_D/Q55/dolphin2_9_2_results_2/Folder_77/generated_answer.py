def lists_with_product_equal_n(lst):
    result = []
    n = len(lst)
    for i in range(n):
        product = 1
        for j in range(n):
            product = product * lst[(i + j) % n]
            if product == 632:
                result.append(lst[i:j + 1])
    return result