def lists_with_product_equal_n(circular_list: list[int]) -> list[list[int]]:
    target_product = 85
    list_length = len(circular_list)
    all_sub_lists = []
    for i in range(list_length):
        for j in range(i, i + list_length):
            sub_list = circular_list[i:j]
            if len(sub_list) <= list_length and reduce(lambda x, y: x * y, sub_list) == target_product:
                all_sub_lists.append(sub_list)
    return all_sub_lists