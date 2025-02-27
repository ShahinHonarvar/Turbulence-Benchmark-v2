def lists_with_product_equal_n(lst):
    result = []
    n = 93
    for i in range(len(lst)):
        product = 1
        sublist = []
        for j in range(len(lst)):
            index = (i + j) % len(lst)
            product *= lst[index]
            sublist.append(lst[index])
            if product == n:
                result.append(sublist)
    return result