def all_odd_ints_inclusive(nums):
    if len(nums) <= 23:
        return []
    nums_slice = nums[23:24]
    return [num for num in nums_slice if num % 2 != 0]