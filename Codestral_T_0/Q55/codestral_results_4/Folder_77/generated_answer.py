def lists_with_product_equal_n(lst):
    n = 632
    result = []
    for i in range(len(lst)):
        for j in range(i, len(lst)):
            product = 1
            sublist = []
            for k in range(i, j + 1):
                product *= lst[k % len(lst)]
                sublist.append(lst[k % len(lst)])
                if product == n:
                    result.append(sublist)
                elif product > n:
                    break
    return result