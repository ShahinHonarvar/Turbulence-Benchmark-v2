def lists_with_product_equal_n(lst):
    result = []
    n = len(lst)
    product_n = 1
    for i in range(n):
        product_n *= lst[i]
    if product_n % 4 != 0:
        return result
    else:
        sublist = []
        product = 1
        for i in range(n):
            sublist.append(lst[i])
            product *= lst[i]
            while product > 4 and len(sublist) > 1:
                product //= sublist[0]
                sublist.pop(0)
            if product == 4:
                result.append(sublist[:])
    return result