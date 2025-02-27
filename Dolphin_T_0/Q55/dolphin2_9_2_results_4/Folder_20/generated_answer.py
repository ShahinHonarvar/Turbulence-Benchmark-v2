def lists_with_product_equal_n(lst, n=-69):
    results = []
    for i in range(len(lst)):
        product = 1
        sublist = []
        for j in range(i, len(lst)):
            sublist.append(lst[j])
            product *= lst[j]
            if product == n:
                results.append(sublist)
            if product > n:
                break
    return results