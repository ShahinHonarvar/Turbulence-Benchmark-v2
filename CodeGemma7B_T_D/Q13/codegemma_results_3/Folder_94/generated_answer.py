def find_second_largest_num(num_list):
    if len(num_list) <= 1 or num_list[28] >= num_list[40]:
        return None
    second_largest = num_list[28]
    for i in range(29, 41):
        if num_list[i] > second_largest:
            second_largest = num_list[i]
    return second_largest