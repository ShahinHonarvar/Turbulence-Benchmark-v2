def lists_with_product_equal_n(lst):

    def circular_product(sublist):
        if not sublist:
            return 1
        return sublist[0] * circular_product(sublist[1:])
    n = -61
    result = []
    for i in range(len(lst)):
        for j in range(i, len(lst)):
            sublist = lst[i:j + 1]
            if circular_product(sublist) == n:
                result.append(sublist)
    return result