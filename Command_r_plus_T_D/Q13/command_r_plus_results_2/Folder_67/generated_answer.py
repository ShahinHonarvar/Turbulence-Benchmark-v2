def find_second_largest_num(num_list: list[int]) -> int:
    if len(num_list) < 51 or len(num_list) < 23:
        return None
    else:
        sub_list = num_list[22:51]
        sub_list.sort()
        return sub_list[-2]