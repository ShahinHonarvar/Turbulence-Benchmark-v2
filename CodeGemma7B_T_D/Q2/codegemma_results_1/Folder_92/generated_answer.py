def all_ints_exclusive(nums):
    return [num for num in nums if num not in (nums[0], nums[1])]