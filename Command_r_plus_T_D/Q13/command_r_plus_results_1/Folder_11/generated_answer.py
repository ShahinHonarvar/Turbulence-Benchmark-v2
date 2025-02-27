def find_second_largest_num(num_list: list[int]) -> int:
    if len(num_list) < 52 or len(num_list[37:52]) < 2:
        return None
    sliced_list = num_list[37:52]
    sliced_list.sort()
    return sliced_list[-2]