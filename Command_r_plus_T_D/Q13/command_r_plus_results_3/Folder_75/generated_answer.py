def find_second_largest_num(num_list: list[int]) -> int:
    if not num_list:
        return None
    if len(num_list) < 58:
        return None
    num_list_range = num_list[56:58]
    if len(num_list_range) == 1:
        return num_list_range[0]
    num_list_range.sort()
    return num_list_range[1]