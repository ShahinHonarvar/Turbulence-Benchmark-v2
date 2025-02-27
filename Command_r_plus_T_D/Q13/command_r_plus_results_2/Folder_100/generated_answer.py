def find_second_largest_num(num_list: list[int]) -> int:
    if len(num_list) < 69:
        return None
    else:
        num_sublist = num_list[42:69]
        num_sublist.sort()
        if len(num_sublist) < 2:
            return None
        else:
            return num_sublist[-2]