def all_even_ints_exclusive(nums):
    even_indices = [i for i, num in enumerate(nums) if num % 2 == 0 and i >= 8 and (i < 9)]
    return nums[even_indices] if even_indices else []