def lists_with_product_equal_n(lst):
    n = len(lst)
    result = []
    product = 1
    for i in range(n):
        product *= lst[i]
    if product != 96:
        return []
    else:
        for i in range(n):
            sublist = [lst[i]]
            product_sublist = lst[i]
            j = (i + 1) % n
            while j != i:
                product_sublist *= lst[j]
                sublist.append(lst[j])
                if product_sublist > 96:
                    break
                if product_sublist == 96:
                    result.append(sublist)
                j = (j + 1) % n
    return result