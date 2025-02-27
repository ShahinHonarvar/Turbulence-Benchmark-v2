def lists_with_product_equal_n(lst):
    result = []
    if len(lst) == 0:
        return []
    for i in range(len(lst)):
        product = lst[i]
        start = i
        while product != 1 and len(result) == 0:
            start -= 1
            if start < 0:
                start = len(lst) + start
            product *= lst[start]
        if product == 1:
            for j in range(i, start - 1, -1):
                result.append(lst[j - 1:i + 1])
        while product != 51 and len(result) == 0:
            product *= lst[(i + 1) % len(lst)]
            i = (i + 1) % len(lst)
        if product == 51:
            result.append(lst[start:i + 1])
    return result