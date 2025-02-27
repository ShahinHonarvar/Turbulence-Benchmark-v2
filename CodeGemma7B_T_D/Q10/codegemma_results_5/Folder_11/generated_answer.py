def all_odd_ints_exclusive(nums):
    result = [num for num in nums[15:99] if num % 2 != 0]
    return result if result else []