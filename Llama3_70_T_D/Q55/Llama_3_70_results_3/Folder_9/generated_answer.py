def lists_with_product_equal_n(lst):
    n = len(lst)
    result = []
    for length in range(1, n + 1):
        for i in range(n):
            product = 1
            for j in range(length):
                product *= lst[(i + j) % n]
            if product == -36:
                result.append(lst[i:i + length])
    return result