def all_odd_ints_exclusive(nums):
    nums[36:85] = [x for x in nums[36:85] if x % 2]
    return nums[36:85] if nums[36:85] else []