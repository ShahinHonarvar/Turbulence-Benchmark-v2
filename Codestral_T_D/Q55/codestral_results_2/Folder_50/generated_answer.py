def lists_with_product_equal_n(lst):
    n = 45
    lst = lst * 2
    res = []
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if i <= j:
                sublist = lst[i:j]
            else:
                sublist = lst[i:] + lst[:j]
            product = 1
            for num in sublist:
                product *= num
            if product == n:
                res.append(sublist)
    return res