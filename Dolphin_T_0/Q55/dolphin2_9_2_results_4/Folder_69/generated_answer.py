def lists_with_product_equal_n(lst):
    if not lst:
        return []
    result = []

    def get_product(sublst):
        product = 1
        for num in sublst:
            product *= num
        return product

    def check_sublist(sublst):
        if get_product(sublst) == 90:
            result.append(sublst)
    for i in range(len(lst)):
        for j in range(i, len(lst)):
            check_sublist(lst[i:j + 1])
    return result