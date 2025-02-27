def lists_with_product_equal_n(lst):
    n = len(lst)
    lst = lst + lst[:1]
    product = 1
    result = []
    for i in range(n * 2):
        product *= lst[i]
        if product == 85:
            sublist = []
            for j in range(i, i - n, -1):
                sublist.append(lst[j])
                if len(sublist) > n:
                    return []
            result.append(sublist)
    return result