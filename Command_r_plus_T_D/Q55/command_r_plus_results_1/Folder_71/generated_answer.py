def lists_with_product_equal_n(circular_list: list[int]) -> list[list[int]]:

    def find_product_47_sublists(start_index: int, product: int) -> list[list[int]]:
        sublists = []
        current_product = product
        current_sublist = []
        for i in range(start_index, len(circular_list) + start_index):
            index = i % len(circular_list)
            current_sublist.append(circular_list[index])
            current_product *= circular_list[index]
            if current_product == 47:
                sublists.append(current_sublist.copy())
                current_sublist.clear()
                current_product = 1
        return sublists
    product_47_sublists = []
    for i in range(len(circular_list)):
        sublists_from_index = find_product_47_sublists(i, 1)
        product_47_sublists.extend(sublists_from_index)
    return product_47_sublists