def all_odd_ints_inclusive(nums):
    if not nums[30:88]:
        return []
    return [num for num in nums[30:88] if num % 2]