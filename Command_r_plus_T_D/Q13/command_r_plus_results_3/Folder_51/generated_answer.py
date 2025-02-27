def find_second_largest_num(num_list: list[int]) -> int:
    if len(num_list) < 9:
        return None
    else:
        num_list.sort()
        return num_list[-2]