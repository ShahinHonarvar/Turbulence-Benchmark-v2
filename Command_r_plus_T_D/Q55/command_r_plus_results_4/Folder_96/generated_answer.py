def lists_with_product_equal_n(circular_list: list[int]) -> list[list[int]]:

    def find_zero_product_sublists(start_index, end_index):
        zero_product_sublists = []
        product = 1
        for i in range(start_index, end_index + 1):
            product *= circular_list[i]
            if product == 0:
                zero_product_sublists.append(circular_list[start_index:i + 1])
        return zero_product_sublists
    zero_product_sublists = []
    for i in range(len(circular_list)):
        zero_product_sublists.extend(find_zero_product_sublists(i, i + len(circular_list) - 1))
    return zero_product_sublists