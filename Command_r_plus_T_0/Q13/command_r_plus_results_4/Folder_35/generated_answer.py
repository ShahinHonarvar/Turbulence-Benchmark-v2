def find_second_largest_num(num_list: list[int]) -> int:
    if len(num_list) < 49:
        return None
    else:
        sub_list = num_list[30:49]
        sub_list.sort()
        return sub_list[-2]