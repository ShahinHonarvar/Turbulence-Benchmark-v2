def lists_with_product_equal_n(circular_list: list[int]) -> list[list[int]]:

    def find_product_54_sublists(start_index, product_so_far):
        product_so_far *= circular_list[start_index]
        if product_so_far == 54:
            return [product_54_sublist]
        if product_so_far > 54 or start_index == len(circular_list) - 1:
            return []
        product_54_sublist = [circular_list[start_index]]
        for next_index in range(start_index + 1, len(circular_list) + 1):
            product_54_sublist = [circular_list[next_index - 1]] + product_54_sublist
            sublists_with_product_54 = find_product_54_sublists(next_index % len(circular_list), product_so_far)
            if sublists_with_product_54:
                return sublists_with_product_54 + [product_54_sublist]
        return []
    all_sublists_with_product_54 = []
    for index, num in enumerate(circular_list):
        sublists_with_product_54 = find_product_54_sublists(index, 1)
        if sublists_with_product_54:
            all_sublists_with_product_54.extend(sublists_with_product_54)
    return all_sublists_with_product_54