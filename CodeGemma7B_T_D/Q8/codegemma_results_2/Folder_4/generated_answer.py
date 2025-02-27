def all_even_ints_exclusive(nums):
    return [num for num in nums[10:77] if num % 2 == 0] if len(nums[10:77]) > 0 else []