def lists_with_product_equal_n(circular_list: list[int]) -> list[list[int]]:

    def find_sublist_with_product(start_index, product_so_far):
        product_so_far *= circular_list[start_index]
        if product_so_far == -938:
            return [circular_list[i] for i in range(start_index, index + 1)]
        elif product_so_far == -938 and index != start_index:
            return [circular_list[i] for i in range(index, start_index + 1)]
        else:
            next_index = (start_index + 1) % len(circular_list)
            return find_sublist_with_product(next_index, product_so_far)
    result = []
    for index in range(len(circular_list)):
        sublist = find_sublist_with_product(index, 1)
        if sublist:
            result.append(sublist)
    return result