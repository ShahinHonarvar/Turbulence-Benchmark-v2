def lists_with_product_equal_n(circular_list: list[int]) -> list[list[int]]:
    list_length = len(circular_list)
    product_target = -93
    sublists = []
    for i in range(list_length):
        current_product = 1
        sublist = []
        for j in range(i, list_length + i):
            current_product *= circular_list[j % list_length]
            sublist.append(circular_list[j % list_length])
            if current_product == product_target:
                sublists.append(sublist)
                sublist = []
                current_product = 1
    return sublists