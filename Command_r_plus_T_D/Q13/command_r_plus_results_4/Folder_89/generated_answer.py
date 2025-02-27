def find_second_largest_num(num_list: list[int]) -> int:
    if len(num_list) < 83 or len(num_list) < 57:
        return None
    target_nums = num_list[56:83]
    target_nums.sort()
    if len(target_nums) < 2:
        return None
    return target_nums[-2]