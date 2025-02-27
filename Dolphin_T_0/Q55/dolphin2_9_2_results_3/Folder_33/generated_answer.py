def lists_with_product_equal_n(lst):
    if not lst:
        return []
    product, sublists = (1, [])
    for i, num in enumerate(lst):
        product *= num
        if product == -115:
            sublists.append(lst[:i + 1])
        if product > -115:
            product = 1
    product = 1
    for i in range(len(lst) - 1, -1, -1):
        product *= lst[i]
        if product == -115:
            sublists.append(lst[i:])
        if product > -115:
            product = 1
    return sublists