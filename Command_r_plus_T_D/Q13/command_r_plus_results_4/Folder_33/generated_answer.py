def find_second_largest_num(num_list: list[int]) -> int:
    if not num_list:
        return None
    try:
        target_range = num_list[667:775]
        target_range.sort()
        return target_range[-2]
    except IndexError:
        return None