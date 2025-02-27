def lists_with_product_equal_n(lst):
    n = -9
    result = []
    for i in range(len(lst)):
        if lst[i] == n:
            result.append([lst[i]])
        product = 1
        for j in range(i + 1, len(lst) + i):
            product *= lst[j % len(lst)]
            if product == n:
                result.append(lst[i:j % len(lst) + 1])
    return result