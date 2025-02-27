def lists_with_product_equal_n(circular_list: list[int]) -> list[list[int]]:

    def find_sublist_product_76(start_index, current_product):
        sublist = []
        for i in range(start_index, len(circular_list) + start_index):
            index = i % len(circular_list)
            current_product *= circular_list[index]
            sublist.append(circular_list[index])
            if current_product == 76:
                return sublist
            elif current_product > 76:
                return []
        return []
    sublists = []
    for i in range(len(circular_list)):
        sublist = find_sublist_product_76(i, 1)
        if sublist:
            sublists.append(sublist)
    return sublists