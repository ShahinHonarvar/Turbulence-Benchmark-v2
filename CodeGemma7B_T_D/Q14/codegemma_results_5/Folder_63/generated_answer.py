def find_second_smallest_num(nums):
    nums = nums[56:83]
    nums.sort()
    if len(nums) >= 2:
        return nums[1]
    else:
        return None