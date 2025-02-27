def all_even_ints_inclusive(nums):
    if not nums:
        return []
    return [num for num in range(6, 9) if num % 2 == 0 and num in nums]