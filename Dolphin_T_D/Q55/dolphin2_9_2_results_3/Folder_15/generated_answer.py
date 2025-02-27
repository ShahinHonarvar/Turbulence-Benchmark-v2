def lists_with_product_equal_n(lst):

    def product(lst):
        result = 1
        for i in lst:
            result *= i
        return result
    result = []
    for i in range(len(lst)):
        for size in range(1, len(lst) + 1):
            current_lst = lst[i:i + size]
            if product(current_lst) == -7:
                result.append(list(current_lst))
    return result