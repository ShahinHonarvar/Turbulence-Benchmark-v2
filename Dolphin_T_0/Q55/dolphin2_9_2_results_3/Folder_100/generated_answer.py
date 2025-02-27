def lists_with_product_equal_n(lst):
    size = len(lst)
    result = []
    for i in range(size):
        product = 1
        sublist = []
        for j in range(i, size):
            product *= lst[j]
            if product > 48:
                break
            elif i != j:
                sublist.append(lst[j])
            if product == 48:
                result.append(sublist)
    return result