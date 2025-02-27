def lists_with_product_equal_n(lst):
    if not lst:
        return []

    def product(lst):
        prod = 1
        for x in lst:
            prod *= x
        return prod
    if product(lst) != 33:
        return []
    result = []
    for x in lst:
        if x == 1:
            result.append([1])
        if x == 33:
            result.append([33])
        for y in lst:
            if product([x, y]) == 33 and [x, y] not in result:
                result.append([x, y])
    return result