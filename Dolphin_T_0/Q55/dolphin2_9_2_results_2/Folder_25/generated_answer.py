def lists_with_product_equal_n(lst, n=-32):
    result = []
    length = len(lst)
    if length == 0:
        return result
    for i in range(length):
        check = 1
        for j in range(i, i + length):
            check *= lst[j % length]
            if check == n and [lst[k] for k in range(i, j + 1)] not in result:
                result.append([lst[k] for k in range(i, j + 1)])
    return result