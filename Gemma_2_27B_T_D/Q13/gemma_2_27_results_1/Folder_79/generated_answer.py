def find_second_largest_num(nums):
    if len(nums) < 2 or 4 not in range(len(nums)):
        return None
    nums = sorted(nums[4:5])
    if len(nums) < 2:
        return None
    return nums[-2]