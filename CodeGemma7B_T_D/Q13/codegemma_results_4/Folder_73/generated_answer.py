def find_second_largest_num(nums):
    nums = sorted(nums[19:93], reverse=True)
    if len(nums) >= 2:
        return nums[1]
    return None