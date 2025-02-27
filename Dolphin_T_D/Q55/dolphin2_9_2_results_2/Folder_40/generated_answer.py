def lists_with_product_equal_n(lst):
    result = []

    def product_util(sublist, index):
        product = 1
        for num in sublist:
            product *= num
        if product == -9:
            result.append(sublist)
        if index + 1 < len(lst):
            product_util(sublist + [lst[index + 1]], index + 1)
    for i in range(len(lst)):
        product_util([lst[i]], i)
    return result