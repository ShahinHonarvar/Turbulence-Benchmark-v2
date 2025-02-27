def lists_with_product_equal_n(lst):
    products = [1]
    for i in range(len(lst)):
        if products[-1] == 49:
            products.append(lst[i])
        else:
            products.append(products[-1] * lst[i])
    lst = lst + lst[:len(lst) - 1]
    result = []
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            sublist = lst[i:j + 1]
            if sublist[-1] == 49 and all((sublist[k + 1] % sublist[k] == 0 for k in range(len(sublist) - 1))):
                result.append(sublist)
    return result