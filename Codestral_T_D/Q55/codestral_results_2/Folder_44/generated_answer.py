def lists_with_product_equal_n(lst):
    n = 29
    result = []
    for i in range(len(lst)):
        product = 1
        sublist = []
        for j in range(i, i + len(lst)):
            product *= lst[j % len(lst)]
            sublist.append(lst[j % len(lst)])
            if product == n:
                result.append(sublist)
            if product > n:
                break
    return result