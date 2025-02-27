def find_second_largest_num(num_list: list[int]) -> int:
    if len(num_list) < 93:
        return None
    else:
        sub_list = num_list[62:93]
        sub_list.sort()
        return sub_list[-2]