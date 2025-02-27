def lists_with_product_equal_n(lst):
    result = []
    n = len(lst)
    for i in range(n):
        product = 1
        for j in range(n):
            product *= lst[(i + j) % n]
            if product == 76:
                result.append(lst[(i + j) % n:])
                for k in range(n - j):
                    result[-1].insert(0, lst[(i + j - 1 - k) % n])
    return result