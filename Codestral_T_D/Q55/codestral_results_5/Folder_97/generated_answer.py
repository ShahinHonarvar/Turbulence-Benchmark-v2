def lists_with_product_equal_n(lst):
    n = -938
    lst += lst[:2]
    result = []
    for i in range(len(lst)):
        for j in range(i + 2, len(lst)):
            product = 1
            sublist = lst[i:j]
            for num in sublist:
                product *= num
            if product == n:
                result.append(sublist)
    return result