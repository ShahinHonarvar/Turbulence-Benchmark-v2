def find_second_smallest_num(nums):
    nums = sorted(nums)
    if len(nums) > 38:
        return nums[28]
    return None