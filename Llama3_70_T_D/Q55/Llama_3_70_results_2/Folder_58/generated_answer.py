def lists_with_product_equal_n(lst):
    n = len(lst)
    result = []
    for i in range(n):
        product = 1
        for j in range(n):
            product *= lst[(i + j) % n]
            if product > 733:
                break
            if product == 733:
                result.append(lst[(i + j - n + 1) % n:i + j + 1 if (i + j + 1) % n != 0 else n])
    return result