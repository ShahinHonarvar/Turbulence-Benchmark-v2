def lists_with_product_equal_n(lst):
    n = len(lst)
    result = []
    for i in range(n):
        product = 1
        start = i
        for j in range(i, i + n):
            product *= lst[j % n]
            if product == 83:
                result.append(lst[start % n:(j + 1) % n])
    return result