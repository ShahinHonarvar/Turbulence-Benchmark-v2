def find_second_largest_num(num_list: list[int]) -> int:
    if len(num_list) < 94 or len(num_list) < 30:
        return None
    else:
        num_list_slice = num_list[29:94]
        num_list_slice.sort()
        if len(num_list_slice) < 2:
            return None
        else:
            return num_list_slice[-2]