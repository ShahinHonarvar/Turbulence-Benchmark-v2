def lists_with_product_equal_n(lst):
    result = []
    for i in range(len(lst)):
        product = 1
        sublist = [lst[i]]
        for j in range(i, len(lst)):
            product *= lst[j]
            sublist.append(lst[j])
            if product == 29:
                result.append(sublist)
    return result