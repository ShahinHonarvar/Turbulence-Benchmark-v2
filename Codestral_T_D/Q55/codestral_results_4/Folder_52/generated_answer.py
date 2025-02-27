def lists_with_product_equal_n(lst):

    def is_product_n(sublst):
        product = 1
        for num in sublst:
            product *= num
        return product == 37
    n = len(lst)
    result = []
    for i in range(n):
        for j in range(i, n):
            sublst = lst[i:j + 1] + lst[:i] if i > j else lst[i:j + 1]
            if is_product_n(sublst):
                if sublst not in result:
                    result.append(sublst)
    return result