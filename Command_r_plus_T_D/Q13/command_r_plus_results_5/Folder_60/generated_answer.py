def find_second_largest_num(num_list: list[int]) -> int:
    if not num_list:
        return None
    target_nums = num_list[75:86]
    target_nums.sort()
    if len(target_nums) < 2:
        return None
    return target_nums[-2]