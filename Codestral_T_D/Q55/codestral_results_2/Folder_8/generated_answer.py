def lists_with_product_equal_n(lst):
    n = -41
    result = []
    for i in range(len(lst)):
        prod = 1
        sublist = []
        for j in range(i, len(lst) + i):
            prod *= lst[j % len(lst)]
            sublist.append(lst[j % len(lst)])
            if prod == n:
                result.append(sublist)
            if prod > abs(n):
                break
            if prod < n:
                continue
            prod = prod // sublist[-1]
            sublist.pop()
    return result