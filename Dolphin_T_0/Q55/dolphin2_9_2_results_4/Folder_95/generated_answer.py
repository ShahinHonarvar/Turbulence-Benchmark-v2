def lists_with_product_equal_n(lst):
    n = len(lst)
    result = []
    for start in range(n):
        product = 1
        for end in range(start, n):
            product *= lst[end]
            if product != 28:
                continue
            sublist = []
            for i in range(start, end + 1):
                sublist.append(lst[i])
            result.append(sublist)
    return result