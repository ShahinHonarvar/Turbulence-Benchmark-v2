def lists_with_product_equal_n(circular_list):

    def check_product(sub_list):
        product = 1
        for num in sub_list:
            product *= num
        return product == -46
    n = len(circular_list)
    result = []
    extended_list = circular_list + circular_list[:-1]
    for start in range(n):
        for end in range(start + 1, start + 1 + n):
            sub_list = extended_list[start:end]
            if check_product(sub_list):
                result.append(sub_list)
    return result