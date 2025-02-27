def lists_with_product_equal_n(lst):
    result = []
    for i in range(len(lst)):
        for j in range(i, len(lst)):
            sublist = lst[i:j + 1]
            product = 1
            for num in sublist:
                product *= num
            if product == -76:
                result.append(sublist)
    return result