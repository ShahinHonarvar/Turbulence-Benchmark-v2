def all_even_ints_exclusive(nums):
    if len(nums) < 97 or len(nums) > 99:
        return []
    return [num for num in nums[69:97] if num % 2 == 0]