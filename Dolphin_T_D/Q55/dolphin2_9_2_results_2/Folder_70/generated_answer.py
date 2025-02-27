def lists_with_product_equal_n(lst):
    result = []
    size = len(lst)
    for i in range(size):
        for j in range(i + 1, size + 1):
            sublst = lst[i:j]
            product = 1
            for num in sublst:
                product *= num
            if product == 32:
                result.append(sublst)
    return result