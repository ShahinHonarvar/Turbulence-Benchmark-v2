def all_even_ints_exclusive(nums):
    if not any((num % 2 == 0 and 10 < idx < 100 for idx, num in enumerate(nums))):
        return []
    return [num for idx, num in enumerate(nums) if num % 2 == 0 and 10 < idx < 100]