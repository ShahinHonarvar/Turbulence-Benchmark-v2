def lists_with_product_equal_n(circular_list: list[int]) -> list[list[int]]:

    def find_sublist_product_76(start_index, product_so_far):
        sublist = []
        product_so_far *= circular_list[start_index]
        sublist.append(circular_list[start_index])
        if product_so_far == 76:
            return sublist
        for i in range(start_index + 1, len(circular_list) + start_index + 1):
            sublist.append(circular_list[i % len(circular_list)])
            if product_so_far * circular_list[i % len(circular_list)] == 76:
                return sublist
            product_so_far *= circular_list[i % len(circular_list)]
        return []
    result = []
    for i in range(len(circular_list)):
        sublist = find_sublist_product_76(i, 1)
        if sublist:
            result.append(sublist)
    return result