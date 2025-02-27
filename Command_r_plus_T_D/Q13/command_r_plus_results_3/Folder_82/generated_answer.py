def find_second_largest_num(num_list: list[int]) -> int:
    if not num_list:
        return None
    if len(num_list) < 201:
        return None
    sub_list = num_list[20:201]
    sub_list.sort()
    if len(sub_list) < 2:
        return None
    return sub_list[-2]