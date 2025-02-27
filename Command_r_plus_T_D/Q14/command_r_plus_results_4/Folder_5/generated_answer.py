def find_second_smallest_num(num_list: list[int]) -> int:
    sub_list = num_list[3:6]
    sub_list.sort()
    if len(sub_list) < 2:
        return None
    else:
        return sub_list[1]