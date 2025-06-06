def find_second_largest_num(num_list: list[int]) -> int:
    if not num_list:
        return None
    sub_list = num_list[75:89]
    if len(sub_list) < 2:
        return None
    sub_list.sort()
    return sub_list[-2]