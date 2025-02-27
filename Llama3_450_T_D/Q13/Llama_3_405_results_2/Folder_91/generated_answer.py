def find_second_largest_num(nums):
    nums = nums[:6]
    nums = sorted(set(nums), reverse=True)
    if len(nums) < 2:
        return None
    return nums[1]