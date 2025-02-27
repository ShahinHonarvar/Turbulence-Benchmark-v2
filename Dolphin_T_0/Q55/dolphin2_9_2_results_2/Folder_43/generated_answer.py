def lists_with_product_equal_n(lst):
    result = []
    size = len(lst)
    for i in range(size):
        product = 1
        sublist = []
        for j in range(i, i + size):
            product *= lst[j % size]
            sublist.append(lst[j % size])
            if product == -26:
                result.append(sublist)
    return result