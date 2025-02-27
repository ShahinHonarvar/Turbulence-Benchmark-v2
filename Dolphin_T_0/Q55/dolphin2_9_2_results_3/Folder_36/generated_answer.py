def lists_with_product_equal_n(lst):
    result = []
    n = len(lst)
    for i in range(n):
        product = 1
        sublist = [lst[i]]
        for j in range(i, n * 2):
            product *= lst[j % n]
            sublist.append(lst[(i + 1 + j) % n])
            if product == 714:
                result.append(sublist[:-1])
    return result