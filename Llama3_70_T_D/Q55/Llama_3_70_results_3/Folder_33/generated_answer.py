def lists_with_product_equal_n(lst):
    n = len(lst)
    result = []
    for length in range(1, n + 1):
        product = 1
        for i in range(length):
            product *= lst[i]
        if product == -115:
            result.append(lst[:length])
        for i in range(1, n):
            product = product * lst[(i + length - 1) % n] / lst[i - 1]
            if product == -115:
                result.append(lst[i:i + length])
    return result