def lists_with_product_equal_n(circular_list: list[int]) -> list[list[int]]:

    def find_product_sublists(start_index: int, product: int) -> list[list[int]]:
        sublists = []
        current_product = 1
        current_sublist = []
        for i in range(start_index, len(circular_list) + start_index):
            index = i % len(circular_list)
            current_sublist.append(circular_list[index])
            current_product *= circular_list[index]
            if current_product == product:
                sublists.append(current_sublist.copy())
                current_sublist.pop(0)
                current_product //= circular_list[index]
        return sublists
    product_to_find = 247
    sublists_with_product = []
    for i in range(len(circular_list)):
        sublists_with_product.extend(find_product_sublists(i, product_to_find))
    return sublists_with_product