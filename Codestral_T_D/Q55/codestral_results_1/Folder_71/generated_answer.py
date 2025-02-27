def lists_with_product_equal_n(lst):
    n = 47
    sublists = []
    for i in range(len(lst)):
        for j in range(i, len(lst)):
            product = 1
            sublist = lst[i:j + 1]
            if i > j:
                sublist += lst[:i]
            for num in sublist:
                product *= num
            if product == n:
                sublists.append(sublist)
    return sublists