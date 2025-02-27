def find_second_largest_num(num_list: list[int]) -> int:
    if not num_list:
        return None
    target_range = num_list[34:56]
    if len(target_range) < 2:
        return None
    target_range.sort()
    return target_range[-2]