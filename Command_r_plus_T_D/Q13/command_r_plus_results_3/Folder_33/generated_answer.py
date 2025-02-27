def find_second_largest_num(num_list: list[int]) -> int:
    if not num_list:
        return None
    if len(num_list) < 775:
        return None
    sliced_list = num_list[667:775]
    sliced_list.sort()
    if len(sliced_list) < 2:
        return None
    return sliced_list[-2]