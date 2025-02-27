def all_even_ints_exclusive(nums):
    return [num for num in nums[0:11] if isinstance(num, int) and num % 2 == 0]