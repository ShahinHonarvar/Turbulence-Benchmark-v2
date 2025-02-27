def lists_with_product_equal_n(lst):
    if len(lst) == 0:
        return []
    result = []
    for i in range(len(lst)):
        product = lst[i]
        if product == 27:
            result.append([lst[i]])
        sublist = [lst[i]]
        for j in range(i + 1, i + len(lst)):
            sublist.append(lst[j % len(lst)])
            product *= lst[j % len(lst)]
            if product == 27:
                result.append(sublist)
            if product > 27:
                break
    return result