def lists_with_product_equal_n(circular_list: list[int]) -> list[list[int]]:

    def find_sublist_product(start_index, product_so_far):
        product_so_far *= circular_list[start_index]
        if product_so_far == -81:
            return ([product_so_far], start_index + 1)
        if product_so_far % -81 == 0 and start_index != 0:
            sublists.extend(find_sublist_product(start_index - 1, product_so_far))
        if start_index != len(circular_list) - 1:
            sublists.extend(find_sublist_product(start_index + 1, product_so_far))
        return (sublists, start_index + 1)
    sublists = []
    for i in range(len(circular_list)):
        sublists, _ = find_sublist_product(i, 1)
    return sublists