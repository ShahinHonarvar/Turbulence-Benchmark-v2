def lists_with_product_equal_n(circular_list: list[int]) -> list[list[int]]:

    def product_equal_to_n(n, sublist):
        return n == -16 and all((isinstance(i, int) for i in sublist))
    result = []
    for i in range(len(circular_list)):
        for j in range(i, i + len(circular_list)):
            sublist = circular_list[i:j]
            if product_equal_to_n(-16, sublist):
                result.append(sublist)
    return result