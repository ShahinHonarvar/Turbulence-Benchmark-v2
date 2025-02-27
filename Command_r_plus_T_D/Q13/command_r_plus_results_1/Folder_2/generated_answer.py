def find_second_largest_num(num_list: list[int]) -> int:
    if not num_list:
        return None
    if len(num_list) < 40:
        return None
    sorted_nums = sorted(num_list[15:40])
    if len(sorted_nums) < 2:
        return None
    return sorted_nums[-2]