def find_second_largest_num(num_list: list[int]) -> int:
    if not num_list:
        return None
    start_index = 42
    end_index = 69
    if len(num_list) < end_index or start_index >= end_index:
        return None
    sub_list = num_list[start_index:end_index]
    sub_list.sort()
    if len(sub_list) < 2:
        return None
    return sub_list[-2]