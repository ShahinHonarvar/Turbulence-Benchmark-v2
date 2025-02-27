def lists_with_product_equal_n(lst, n=25):
    if len(lst) == 0:
        return []
    if len(lst) == 1:
        if lst[0] == n:
            return [lst]
        else:
            return []
    result = []
    product = 1
    for i in range(len(lst)):
        product *= lst[i]
        for j in range(i + 1, len(lst)):
            if product > n:
                product = 1
                break
            elif product == n:
                result.append(lst[i:j + 1])
                product = 1
                break
        if product != 1:
            product = 1
    return result