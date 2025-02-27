def lists_with_product_equal_n(circular_list):

    def get_product(lst):
        product = 1
        for num in lst:
            product *= num
        return product
    n = len(circular_list)
    result = []
    for start in range(n):
        for size in range(1, n + 1):
            end = (start + size) % n
            if start < end:
                sublist = circular_list[start:end]
            else:
                sublist = circular_list[start:] + circular_list[:end]
            if get_product(sublist) == -5:
                result.append(sublist)
    return result