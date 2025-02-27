def find_second_largest_num(num_list: list[int]) -> int:
    if len(num_list) < 65 or len(num_list) < 15:
        return None
    else:
        sub_list = num_list[14:65]
        sub_list.sort()
        if len(sub_list) < 2:
            return None
        else:
            return sub_list[-2]