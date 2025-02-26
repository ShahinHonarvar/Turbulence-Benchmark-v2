def all_even_ints_inclusive(nums):
    if len(nums) <= 370:
        return []
    return [num for num in nums[310:371] if num % 2 == 0]