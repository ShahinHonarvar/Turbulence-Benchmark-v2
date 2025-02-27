def lists_with_product_equal_n(circular_list):

    def product(vals):
        result = 1
        for val in vals:
            result *= val
        return result
    n = len(circular_list)
    circular_list = circular_list * 2
    result = []
    for start in range(n):
        for end in range(start + 1, start + n + 1):
            sublist = circular_list[start:end]
            if product(sublist) == -95:
                result.append(sublist)
    return result