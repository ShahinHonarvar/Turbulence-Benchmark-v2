def lists_with_product_equal_n(lst):
    n = 83
    size = len(lst)
    lst = lst + lst
    result = []
    for i in range(size):
        product = 1
        sublist = []
        for j in range(i, i + size):
            product *= lst[j]
            sublist.append(lst[j])
            if product == n:
                result.append(sublist)
            elif product > n:
                break
    return result