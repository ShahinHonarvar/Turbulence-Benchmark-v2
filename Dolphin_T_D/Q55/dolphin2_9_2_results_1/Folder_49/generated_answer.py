def lists_with_product_equal_n(lst, n=-61):
    result = []
    length = len(lst)
    if length < 1:
        return result
    for i in range(length):
        for j in range(i, length):
            sublist = []
            product = 1
            for k in range(i, j + 1):
                sublist.append(lst[k % length])
                product *= lst[k % length]
            if product == n:
                result.append(sublist)
    return result