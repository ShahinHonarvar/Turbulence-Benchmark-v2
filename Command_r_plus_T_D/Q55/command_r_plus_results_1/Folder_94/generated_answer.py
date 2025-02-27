def lists_with_product_equal_n(circular_list: list[int]) -> list[list[int]]:

    def product_equal_n(start_index: int, product: int) -> list[int]:
        sublist = [circular_list[start_index]]
        current_index = (start_index + 1) % len(circular_list)
        while product * circular_list[current_index] != -30:
            if current_index == start_index:
                return []
            product *= circular_list[current_index]
            sublist.append(circular_list[current_index])
            current_index = (current_index + 1) % len(circular_list)
        return sublist
    result = []
    for i in range(len(circular_list)):
        sublist = product_equal_n(i, circular_list[i])
        if sublist:
            result.append(sublist)
    return result