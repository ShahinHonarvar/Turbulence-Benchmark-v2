def lists_with_product_equal_n(lst):
    lst_extended = lst + lst
    n = 99
    sublists = []
    for i in range(len(lst)):
        product = 1
        for j in range(i, len(lst_extended)):
            product *= lst_extended[j]
            if product == n:
                sublists.append(lst_extended[i:j + 1])
            elif product > n:
                break
    return [sublist for sublist in sublists if len(sublist) <= len(lst)]