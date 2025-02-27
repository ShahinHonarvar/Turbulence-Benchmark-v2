def find_second_largest_num(nums):
    if len(nums) < 100:
        return None
    nums = sorted(nums[91:100], reverse=True)
    if len(nums) < 2:
        return None
    return nums[1]