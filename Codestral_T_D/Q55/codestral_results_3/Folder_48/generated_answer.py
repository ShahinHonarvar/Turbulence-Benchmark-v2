def lists_with_product_equal_n(lst):
    result = []
    n = len(lst)
    for i in range(n):
        product = 1
        sublist = []
        for j in range(i, i + n):
            product *= lst[j % n]
            sublist.append(lst[j % n])
            if product == 990:
                result.append(sublist)
                sublist = []
                break
            elif product > 990:
                break
    return result