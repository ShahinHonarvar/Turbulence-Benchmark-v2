def find_second_largest_num(num_list: list[int]) -> int:
    if not num_list:
        return None
    elif len(num_list) < 58:
        return None
    else:
        sub_list = num_list[56:58]
        sub_list.sort()
        return sub_list[1] if len(sub_list) > 1 else None