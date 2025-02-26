def all_odd_ints_inclusive(nums):
    if len(nums) <= 23:
        return []
    target_num = nums[23]
    return [num for num in nums[23:24] if num % 2 != 0]