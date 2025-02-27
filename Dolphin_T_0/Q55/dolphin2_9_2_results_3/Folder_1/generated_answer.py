def lists_with_product_equal_n(lst):
    n = len(lst)
    result = []
    for i in range(n):
        product = lst[i]
        sublist = [lst[i]]
        j = (i + 1) % n
        while j != i:
            if product * lst[j] == -51:
                sublist.append(lst[j])
                result.append(sublist.copy())
            else:
                sublist.append(lst[j])
                product *= lst[j]
            j = (j + 1) % n
    return result