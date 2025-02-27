def lists_with_product_equal_n(lst, n=-54):
    result = []
    for i in range(len(lst)):
        product = 1
        for j in range(1, len(lst) + 1):
            if i + j <= len(lst):
                product *= lst[i + j - 1]
            else:
                product *= lst[i + j - 1 - len(lst)]
            if product == n and [lst[i + j - 1] for j in range(1, len(lst) + 1)] not in result:
                result.append([lst[i + j - 1] for j in range(1, len(lst) + 1)])
    return result