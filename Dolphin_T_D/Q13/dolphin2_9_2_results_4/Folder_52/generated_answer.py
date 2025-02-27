def find_second_largest_num(lst):
    if 28 <= 38 < len(lst):
        sub_list = lst[28:39]
        unique_nums = list(set(sub_list))
        unique_nums.sort()
        if len(unique_nums) >= 2:
            return unique_nums[1]
    return None