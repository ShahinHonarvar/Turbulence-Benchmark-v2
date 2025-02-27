def find_second_largest_num(num_list: list[int]) -> int:
    if len(num_list) < 6:
        return None
    else:
        target_nums = num_list[3:6]
        target_nums.sort()
        if len(target_nums) < 2:
            return None
        else:
            return target_nums[-2]