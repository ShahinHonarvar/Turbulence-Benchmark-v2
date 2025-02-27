def all_even_ints_exclusive(nums):
    return [num for num in nums[295:573] if num % 2 == 0 and num not in range(295, 573)]