def lists_with_product_equal_n(circular_list: list[int]) -> list[list[int]]:
    target_product = 29
    list_size = len(circular_list)
    all_sublists = []
    for start_index in range(list_size):
        for length in range(1, list_size + 1):
            end_index = (start_index + length) % list_size
            sublist = circular_list[start_index:end_index + 1]
            if length == 1 or sublist[-1] * sublist[0] != target_product:
                product = 1
                for num in sublist:
                    product *= num
                if product == target_product:
                    all_sublists.append(sublist)
    return all_sublists