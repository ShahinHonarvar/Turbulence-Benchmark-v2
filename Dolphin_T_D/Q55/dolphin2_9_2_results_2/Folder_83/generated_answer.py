def lists_with_product_equal_n(lst, n=-57):
    res = []
    length = len(lst)
    sublist = []
    for i in range(length):
        sublist = [lst[i]]
        for j in range(i + 1, length):
            sublist.append(lst[j])
            product = 1
            for k in sublist:
                product *= k
            if product == n:
                res.append(sublist)
    return res