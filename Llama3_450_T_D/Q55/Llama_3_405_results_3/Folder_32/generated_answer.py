def lists_with_product_equal_n(lst):
    n = 76
    result = []
    for i in range(len(lst)):
        product = 1
        for j in range(len(lst)):
            product *= lst[(i + j) % len(lst)]
            if product == n:
                result.append(lst[i:i + j + 1] if i + j + 1 <= len(lst) else lst[i:] + lst[:j - len(lst) + i + 1])
            elif product > n:
                break
    return result