def lists_with_product_equal_n(lst):
    result = []
    n = len(lst)
    for i in range(n):
        product = lst[i]
        if product == 83:
            result.append([lst[i]])
        sublists = [[lst[i]]]
        for j in range(i + 1, n + i):
            product *= lst[j % n]
            if product == 83:
                result.append(sublists + [lst[j % n]])
                sublists = [[lst[i]]]
            elif product < 83:
                sublists.append(lst[j % n])
            else:
                sublists = [[lst[i]]]
    return result