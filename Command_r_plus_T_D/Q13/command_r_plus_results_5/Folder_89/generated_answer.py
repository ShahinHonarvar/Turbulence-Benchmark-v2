def find_second_largest_num(num_list: list[int]) -> int:
    if len(num_list) < 83 or len(num_list) < 57:
        return None
    sub_list = num_list[56:83]
    sub_list.sort()
    if len(sub_list) < 2:
        return None
    return sub_list[-2]