def find_second_largest_num(num_list: list[int]) -> int:
    if not num_list:
        return None
    if len(num_list) < 101:
        return None
    num_list_slice = num_list[10:101]
    num_list_slice.sort()
    if len(num_list_slice) < 2:
        return None
    return num_list_slice[-2]