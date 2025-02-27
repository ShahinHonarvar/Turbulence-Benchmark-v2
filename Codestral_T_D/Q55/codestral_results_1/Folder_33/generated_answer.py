def lists_with_product_equal_n(lst):
    result = []
    n = -115
    for i in range(len(lst)):
        product = lst[i]
        sublist = [lst[i]]
        for j in range(i + 1, i + len(lst)):
            product *= lst[j % len(lst)]
            sublist.append(lst[j % len(lst)])
            if product == n:
                result.append(sublist)
    return result