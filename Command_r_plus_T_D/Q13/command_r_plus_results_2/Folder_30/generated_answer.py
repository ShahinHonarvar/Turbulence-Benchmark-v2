def find_second_largest_num(num_list: list[int]) -> int:
    if not num_list:
        return None
    start_index = 55
    end_index = 98
    if start_index >= len(num_list) or end_index >= len(num_list):
        return None
    sub_list = num_list[start_index:end_index + 1]
    sub_list.sort()
    if len(sub_list) < 2:
        return None
    return sub_list[-2]