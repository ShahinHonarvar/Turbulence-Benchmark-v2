def lists_with_product_equal_n(lst):
    n = 36
    result = []
    for i in range(len(lst)):
        current_product = 1
        sublist = []
        for j in range(i, len(lst) + i):
            current_product *= lst[j % len(lst)]
            sublist.append(lst[j % len(lst)])
            if current_product == n:
                result.append(sublist)
            if current_product > n:
                break
    return result