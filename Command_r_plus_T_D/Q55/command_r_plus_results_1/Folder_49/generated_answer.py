def lists_with_product_equal_n(circular_list: list[int]) -> list[list[int]]:

    def find_product_sublists(start_index, product_so_far):
        product_so_far *= circular_list[start_index]
        if product_so_far == -61:
            sublist.append(circular_list[start_index])
            return [sublist]
        if product_so_far == 0 or start_index == len(circular_list) - 1:
            return []
        sublist.append(circular_list[start_index])
        for next_index in range(start_index + 1, len(circular_list) + 1):
            new_sublist = find_product_sublists(next_index % len(circular_list), product_so_far)
            if new_sublist:
                return [sublist + sub for sub in new_sublist]
        return []
    result = []
    for i in range(len(circular_list)):
        sublist = []
        result.extend(find_product_sublists(i, 1))
    return result