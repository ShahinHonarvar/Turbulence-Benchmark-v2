def lists_with_product_equal_n(lst):
    if len(lst) == 0:
        return []
    product = -93
    result = []
    for i in range(len(lst)):
        if lst[i] == 0 or product % lst[i] != 0:
            continue
        sublst = [lst[i]]
        j = (i - 1) % len(lst)
        for k in range(1, len(lst)):
            if lst[j] == 0 or product / sublst[-1] % lst[j] != 0:
                break
            sublst.append(lst[j])
            if len(sublst) > 1 and sublst[-1] == sublst[0]:
                result.append(sublst)
            j = (j - 1) % len(lst)
    return result