def find_second_largest_num(num_list: list[int]) -> int:
    if len(num_list) < 41 or len(num_list) < 29:
        return None
    sub_list = num_list[28:41]
    sub_list.sort()
    if len(sub_list) < 2:
        return None
    return sub_list[-2]