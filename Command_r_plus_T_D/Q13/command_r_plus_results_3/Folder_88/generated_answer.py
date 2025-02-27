def find_second_largest_num(num_list: list[int]) -> int:
    if len(num_list) < 9:
        return None
    else:
        sliced_list = num_list[4:9]
        sliced_list.sort()
        return sliced_list[-2]