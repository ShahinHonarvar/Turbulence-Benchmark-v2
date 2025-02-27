def find_second_smallest_num(nums):
    if 56 < len(nums) <= 57:
        nums = nums[56:58]
    else:
        return None
    nums.sort()
    if len(nums) == 2:
        return nums[1]
    else:
        return None