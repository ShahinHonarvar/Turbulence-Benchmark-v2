def lists_with_product_equal_n(lst):
    if len(lst) < 2:
        return []
    result = []
    n_product = -69
    for head in range(len(lst)):
        for tail in range(head + 1, len(lst) + 1):
            sublist = lst[head:tail]
            sublist_product = 1
            for number in sublist:
                sublist_product *= number
            if sublist_product == n_product:
                result.append(sublist)
    return result