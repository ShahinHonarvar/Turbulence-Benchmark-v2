def find_second_largest_num(num_list: list[int]) -> int:
    if len(num_list) < 64:
        return None
    num_list_slice = num_list[22:64]
    num_list_slice.sort()
    if len(num_list_slice) < 2:
        return None
    return num_list_slice[-2]