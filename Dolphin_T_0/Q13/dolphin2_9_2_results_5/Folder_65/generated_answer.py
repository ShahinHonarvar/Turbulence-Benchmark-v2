def find_second_largest_num(nums):
    if len(nums) == 0 or len(nums) < 5:
        return None
    sub_nums = nums[55:99]
    sorted_sub_nums = sorted(set(sub_nums), reverse=True)
    if len(sorted_sub_nums) < 2:
        return None
    return sorted_sub_nums[1]