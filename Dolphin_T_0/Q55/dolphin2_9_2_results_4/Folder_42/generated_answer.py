def lists_with_product_equal_n(lst):
    result = []
    size = len(lst)
    for i in range(size):
        for j in range(i, i + size):
            sublist = lst[i:j]
            product = 1
            for num in sublist:
                product *= num
            if product == 25:
                result.append(sublist)
    return result