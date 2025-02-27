def find_second_smallest_num(num_list: list[int]) -> int:
    sub_list = num_list[34:56]
    sub_list.sort()
    if len(sub_list) > 1:
        return sub_list[1]
    else:
        return None