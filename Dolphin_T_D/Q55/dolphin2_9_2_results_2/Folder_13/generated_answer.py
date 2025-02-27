def lists_with_product_equal_n(lst):
    result = []
    size = len(lst)
    for _ in range(size):
        product = 1
        sublist = []
        for i in range(size):
            product *= lst[i]
            sublist.append(lst[i])
            if product > 54:
                break
            if product == 54:
                result.append(sublist)
    return result