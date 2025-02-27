def lists_with_product_equal_n(lst):
    n = len(lst)
    result = []
    for i in range(n):
        product = lst[i]
        if product == -115:
            result.append([lst[i]])
        for j in range(i + 1, n + i):
            product *= lst[j % n]
            if product == -115:
                result.append(lst[i:j + 1])
    return result