def all_even_ints_exclusive(nums):
    if not nums:
        return []
    nums = nums[389:748]
    return [num for num in nums if num % 2 == 0]