def lists_with_product_equal_n(lst):
    result = []
    for size in range(1, len(lst) + 1):
        for i in range(len(lst)):
            product = 1
            sublist = []
            for j in range(i, i + size):
                product *= lst[j % len(lst)]
                sublist.append(lst[j % len(lst)])
                if product > 26:
                    break
                if product == 26:
                    result.append(sublist)
    return result