def lists_with_product_equal_n(lst):
    n = 415
    result = []
    for i in range(len(lst)):
        for j in range(i, len(lst)):
            sublist = lst[i:j + 1] + lst[:(i + j + 1) % len(lst)] if i > j else lst[i:j + 1]
            product = 1
            for num in sublist:
                product *= num
            if product == n:
                result.append(sublist)
    return result