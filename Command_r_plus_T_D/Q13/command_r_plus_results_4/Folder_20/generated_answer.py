def find_second_largest_num(num_list: list[int]) -> int:
    if len(num_list) < 67:
        return None
    sub_list = num_list[56:67]
    sub_list.sort()
    if len(sub_list) < 2:
        return None
    return sub_list[-2]