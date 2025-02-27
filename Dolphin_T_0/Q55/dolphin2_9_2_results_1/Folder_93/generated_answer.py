def lists_with_product_equal_n(lst):

    def checking_product(sublst):
        product = 1
        for num in sublst:
            product *= num
        return product
    result = []
    size = len(lst)
    for i in range(1, size + 1):
        for j in range(size + 1 - i):
            sublist = lst[j:j + i]
            if checking_product(sublist) == -91:
                result.append(sublist)
    return result