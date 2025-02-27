def lists_with_product_equal_n(lst):
    result = []
    n = len(lst)
    lst += lst
    for i in range(n):
        product = 1
        sublist = []
        for j in range(i, i + n):
            product *= lst[j]
            sublist.append(lst[j])
            if product == 733 and len(sublist) <= n:
                result.append(sublist)
            if product >= 733:
                break
    return result