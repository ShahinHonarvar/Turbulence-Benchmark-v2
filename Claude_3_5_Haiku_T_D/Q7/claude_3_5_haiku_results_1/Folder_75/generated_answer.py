def all_even_ints_inclusive(nums):
    if len(nums) <= 57:
        return []
    even_ints = [num for num in nums[56:58] if num % 2 == 0]
    return even_ints