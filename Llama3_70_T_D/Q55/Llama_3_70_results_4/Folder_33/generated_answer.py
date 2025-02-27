def lists_with_product_equal_n(lst):
    result = []
    n = len(lst)
    for i in range(n):
        product = 1
        for j in range(1, n + 1):
            product *= lst[(i + j - 1) % n]
            if product == -115:
                result.append(lst[i:(i + j) % n] if i + j <= n else lst[i:] + lst[:j - i])
            elif product > -115 or abs(product) < 115:
                break
    return result