def find_second_largest_num(num_list: list[int]) -> int:
    if len(num_list) < 557:
        return None
    else:
        sliced_list = num_list[209:557]
        sliced_list.sort()
        return sliced_list[-2]