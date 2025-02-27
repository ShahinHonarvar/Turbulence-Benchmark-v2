def all_even_ints_inclusive(nums):
    if not any((num % 2 == 0 for num in nums[15:39 + 1])):
        return []
    return [num for num in nums[15:39 + 1] if num % 2 == 0]