def find_second_largest_num(nums):
    if len(nums) < 35:
        return None
    target_nums = nums[31:35]
    target_nums.sort(reverse=True)
    if len(target_nums) < 2:
        return None
    return target_nums[1]