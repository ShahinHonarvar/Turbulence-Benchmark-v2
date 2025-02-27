def lists_with_product_equal_n(lst, n=53):
    length = len(lst)
    result = []
    for i in range(length):
        product = 1
        sublist = []
        for j in range(i, i + length):
            product *= lst[j % length]
            sublist.append(lst[j % length])
            if product == n:
                result.append(sublist)
    return result