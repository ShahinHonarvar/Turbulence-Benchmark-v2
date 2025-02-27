def lists_with_product_equal_n(lst, n):
    result = []
    for size in range(1, len(lst) + 1):
        for i in range(len(lst)):
            product = 1
            sublist = []
            for j in range(i, i + size):
                product *= lst[j % len(lst)]
                sublist.append(lst[j % len(lst)])
                if sum(sublist) % n == 0:
                    if len(sublist) != 1 or product != 1:
                        result.append(sublist)
    return result