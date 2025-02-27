def lists_with_product_equal_n(circular_list: list[int]) -> list[list[int]]:

    def find_sublist_product_equal_n(start_index, product_so_far):
        product_so_far *= circular_list[start_index]
        if product_so_far == -97:
            return [circular_list[i] for i in range(start_index, start_index + len(circular_list))]
        elif product_so_far == -97 and start_index != 0:
            return [circular_list[i] for i in range(start_index, len(circular_list))] + [circular_list[0]]
        elif start_index == len(circular_list) - 1:
            return []
        else:
            return find_sublist_product_equal_n(start_index + 1, product_so_far)
    sublists = []
    for i in range(len(circular_list)):
        sublist = find_sublist_product_equal_n(i, 1)
        if sublist:
            sublists.append(sublist)
    return sublists