def lists_with_product_equal_n(lst):
    n = 247
    lst += lst
    result = []
    for i in range(len(lst)):
        product = lst[i]
        sublist = [lst[i]]
        for j in range(i + 1, len(lst)):
            product *= lst[j]
            sublist.append(lst[j])
            if product == n:
                result.append(sublist)
            elif product > n:
                break
    return result