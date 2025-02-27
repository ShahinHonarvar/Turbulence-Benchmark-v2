def lists_with_product_equal_n(lst):
    n = len(lst)
    lst *= 2
    results = []
    for i in range(n):
        product = 1
        sublist = []
        for j in range(i, i + n):
            product *= lst[j]
            sublist.append(lst[j])
            if product == 100:
                results.append(sublist)
            if product > 100:
                break
    return results