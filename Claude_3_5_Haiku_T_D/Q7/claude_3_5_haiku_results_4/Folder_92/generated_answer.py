def all_even_ints_inclusive(nums):
    if len(nums) < 2:
        return [num for num in nums[:len(nums)] if num % 2 == 0]
    return [num for num in nums[0:2] if num % 2 == 0]