def lists_with_product_equal_n(lst):
    size = len(lst)
    if size == 0:
        return []
    elif size == 1:
        if lst[0] == 537:
            return [lst]
        else:
            return []
    result = []
    product = 1
    for i in range(size):
        product *= lst[i]
        if product == 537:
            result.append(lst[0:i + 1])
        if product > 537:
            while product != 537:
                product /= lst[0]
                lst = lst[1:] + [lst[0]]
                if product == 537:
                    result.append(lst[0:i + 1])
    return result