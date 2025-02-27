def find_second_largest_num(nums):
    nums = nums[20:31]
    nums.sort(reverse=True)
    return nums[1] if len(nums) >= 2 else 'None'