def lists_with_product_equal_n(lst):
    result = []
    for i in range(len(lst)):
        for j in range(i, len(lst)):
            sublist = lst[i:j + 1]
            product = 1
            for x in sublist:
                product *= x
            if product == 0:
                result.append(sublist)
    return result