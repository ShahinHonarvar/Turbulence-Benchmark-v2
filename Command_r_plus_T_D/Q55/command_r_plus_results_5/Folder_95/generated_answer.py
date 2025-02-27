def lists_with_product_equal_n(circular_list: list[int]) -> list[list[int]]:
    target_product = 28
    list_length = len(circular_list)
    sublists = []
    for i in range(list_length):
        product = 1
        temp_sublist = []
        for j in range(i, list_length + i):
            index = j % list_length
            product *= circular_list[index]
            temp_sublist.append(circular_list[index])
            if product == target_product:
                sublists.append(temp_sublist.copy())
            if product > target_product:
                break
    return sublists