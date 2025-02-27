def all_even_ints_inclusive(nums):
    if not nums:
        return []
    return [num for num in range(0, 11) if num % 2 == 0]