def find_second_largest_num(num_list: list[int]) -> int:
    if not num_list:
        return None
    if len(num_list) < 94 or len(num_list) < 30:
        return None
    target_nums = num_list[29:94]
    target_nums.sort()
    if len(target_nums) < 2:
        return None
    else:
        return target_nums[-2]