def all_even_ints_inclusive(nums):
    if len(nums) <= 774:
        return []
    even_ints = [num for num in nums[667:775] if num % 2 == 0]
    return even_ints