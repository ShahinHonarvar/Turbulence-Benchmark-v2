def lists_with_product_equal_n(lst):
    if len(lst) == 0:
        return []
    product = -968
    result = []
    for i in range(len(lst)):
        temp_product = lst[i]
        sublist = [lst[i]]
        for j in range(i + 1, len(lst)):
            temp_product *= lst[j]
            sublist.append(lst[j])
            if temp_product == product:
                result.append(sublist)
    return result