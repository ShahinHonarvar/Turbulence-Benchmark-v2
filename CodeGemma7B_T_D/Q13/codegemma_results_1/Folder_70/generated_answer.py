def find_second_largest_num(nums):
    nums = nums[28:33]
    nums.remove(max(nums))
    return max(nums) if nums else 'None'