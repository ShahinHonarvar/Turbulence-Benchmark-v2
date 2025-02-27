def lists_with_product_equal_n(lst, n=-7):
    result = []
    size = len(lst)
    for i in range(size):
        for j in range(i + 1, size + 1):
            sublist = lst[i:j]
            product = 1
            for num in sublist:
                product *= num
            if product == n:
                result.append(sublist)
    return result