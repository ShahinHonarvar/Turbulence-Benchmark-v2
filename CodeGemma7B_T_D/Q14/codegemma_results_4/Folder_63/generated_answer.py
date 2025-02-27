def find_second_smallest_num(nums):
    nums = nums[56:83]
    nums.sort()
    return nums[1] if len(nums) >= 2 else 'None'