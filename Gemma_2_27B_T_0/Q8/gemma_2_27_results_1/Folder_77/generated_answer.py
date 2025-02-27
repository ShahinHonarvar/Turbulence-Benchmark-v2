def all_even_ints_exclusive(nums):
    return [num for i, num in enumerate(nums) if i >= 111 and i < 473 and (num % 2 == 0)]