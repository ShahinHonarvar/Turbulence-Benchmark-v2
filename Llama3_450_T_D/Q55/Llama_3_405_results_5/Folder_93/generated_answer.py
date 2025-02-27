def lists_with_product_equal_n(lst):
    n = -91
    result = []
    for i in range(len(lst)):
        product = 1
        for j in range(i, len(lst) + i):
            product *= lst[j % len(lst)]
            if product == n:
                result.append(lst[i:j + 1]) if i < j + 1 else result.append(lst[i:] + lst[:j + 1])
            if product > abs(n) and n < 0 or (product < -abs(n) and n > 0):
                break
    return result