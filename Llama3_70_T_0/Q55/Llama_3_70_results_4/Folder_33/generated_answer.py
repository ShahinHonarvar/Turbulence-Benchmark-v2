def lists_with_product_equal_n(lst):
    n = len(lst)
    result = []
    for i in range(n):
        product = 1
        for j in range(n):
            product *= lst[(i + j) % n]
            if product == -115:
                result.append(lst[(i + j) % n])
            elif product > -115:
                break
    return [lst[i:j + 1] for i in range(n) for j in range(i, n) if lst[i:j + 1] in result]