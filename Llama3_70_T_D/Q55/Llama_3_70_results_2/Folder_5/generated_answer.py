def lists_with_product_equal_n(lst):
    n = len(lst)
    result = []
    for i in range(n):
        product = 1
        for j in range(n):
            product *= lst[(i + j) % n]
            if product == -33:
                result.append(lst[(i + j) % n])
            elif product > -33:
                product = 1
                break
    return [lst[i:i + j + 1] for i, j in {(i, j) for i, j in enumerate(result)}]