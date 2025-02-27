def find_second_largest_num(nums):
    if len(nums[21:98]) < 2:
        return None
    sorted_nums = sorted(nums[21:98])
    return sorted_nums[-2]