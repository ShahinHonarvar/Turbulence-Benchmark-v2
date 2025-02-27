def lists_with_product_equal_n(lst, n=-968):
    result = []
    for i in range(len(lst)):
        for j in range(i + 1, len(lst) + 1):
            if i > j:
                continue
            sublist = lst[i:j]
            sublist_product = 1
            if sublist[0] == 0 and len(sublist) > 1:
                continue
            for num in sublist:
                sublist_product *= num
            if sublist_product == n:
                result.append(sublist)
    return result