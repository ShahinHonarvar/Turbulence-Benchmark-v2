def lists_with_product_equal_n(lst):
    n = -18
    result = []
    length = len(lst)
    for i in range(length):
        product = 1
        for j in range(length):
            product *= lst[(i + j) % length]
            if product == n:
                result.append([lst[(i + k) % length] for k in range(j + 1)])
            elif product > n and n > 0 or (product < n and n < 0):
                break
    return result