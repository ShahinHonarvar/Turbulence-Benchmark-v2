def lists_with_product_equal_n(lst):
    n = len(lst)
    result = []
    for i in range(n):
        product = lst[i]
        if product == 57:
            result.append([lst[i]])
        sublist = [lst[i]]
        for j in range(i + 1, n):
            sublist.append(lst[j])
            product *= lst[j]
            if product == 57:
                result.append(sublist[:])
    for i in range(1, n):
        product = lst[0] * lst[i]
        if product == 57:
            result.append([lst[0], lst[i]])
        sublist = [lst[0], lst[i]]
        for j in range(i + 1, n):
            sublist.append(lst[(j + i) % n])
            product *= lst[(j + i) % n]
            if product == 57:
                result.append(sublist[:])
    return result