def find_second_largest_num(num_list: list[int]) -> int:
    if len(num_list) < 56:
        return None
    else:
        sub_list = num_list[27:56]
        sub_list.sort()
        return sub_list[-2]