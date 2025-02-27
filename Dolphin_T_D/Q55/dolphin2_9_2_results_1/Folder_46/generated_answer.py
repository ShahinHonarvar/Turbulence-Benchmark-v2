def lists_with_product_equal_n(lst):
    if len(lst) == 0:
        return []
    elif len(lst) == 1:
        if lst[0] == 53:
            return [lst]
        else:
            return []
    sublists = []
    for i in range(len(lst)):
        product = 1
        for j in range(i, len(lst)):
            product *= lst[j]
            if product == 53:
                sublists.append(lst[i:j + 1])
            elif product > 53:
                break
    return sublists