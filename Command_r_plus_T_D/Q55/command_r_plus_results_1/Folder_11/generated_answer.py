def lists_with_product_equal_n(circular_list: list[int]) -> list[list[int]]:
    list_length = len(circular_list)
    result = []
    for i in range(list_length):
        for j in range(i, list_length + i):
            sublist = circular_list[i:j]
            if len(sublist) <= list_length and sublist[0] * sublist[-1] == -15:
                result.append(sublist)
    return result