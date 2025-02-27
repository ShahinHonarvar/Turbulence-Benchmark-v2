def lists_with_product_equal_n(lst):
    n = -33
    result = []
    for i in range(len(lst)):
        for j in range(i + 1, i + len(lst)):
            sublist = lst[i:j]
            product = 1
            for num in sublist:
                product *= num
            if product == n:
                result.append(sublist)
    return result