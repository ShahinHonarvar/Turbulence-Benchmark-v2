def find_second_largest_num(num_list: list[int]) -> int:
    if len(num_list[68:87]) < 2:
        return None
    else:
        return sorted(num_list[68:87])[-2]