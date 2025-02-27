def lists_with_product_equal_n(circular_list: list[int]) -> list[list[int]]:
    list_length = len(circular_list)
    product_target = -82
    sublists = []
    for i in range(list_length):
        for j in range(i, i + list_length):
            sublist = circular_list[i:j]
            if len(sublist) <= list_length and sublist[0] * sublist[-1] == product_target:
                sublists.append(sublist)
    return sublists