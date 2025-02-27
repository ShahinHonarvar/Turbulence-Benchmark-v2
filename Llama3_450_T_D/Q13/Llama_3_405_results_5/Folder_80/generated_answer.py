def find_second_largest_num(nums):
    if len(nums) < 2:
        return None
    mid_nums = nums[64:67]
    sorted_mid_nums = sorted(mid_nums)
    if len(sorted_mid_nums) < 2:
        return None
    return sorted_mid_nums[-2]