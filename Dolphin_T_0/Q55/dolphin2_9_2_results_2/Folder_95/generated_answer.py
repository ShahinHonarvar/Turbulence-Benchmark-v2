def lists_with_product_equal_n(lst):
    if len(lst) == 0:
        return []
    lst = lst + lst[:-1]
    result = []
    for i in range(len(lst) - 1):
        product = lst[i]
        sublist = [lst[i]]
        for j in range(i + 1, len(lst)):
            product *= lst[j]
            sublist.append(lst[j])
            if product > 28:
                break
            if product == 28:
                result.append(sublist[:len(lst)])
    return result