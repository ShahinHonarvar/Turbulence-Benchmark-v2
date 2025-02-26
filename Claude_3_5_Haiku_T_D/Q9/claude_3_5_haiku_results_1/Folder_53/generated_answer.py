def all_odd_ints_inclusive(nums):
    if len(nums) < 201:
        return []
    return [num for num in nums[100:201] if num % 2 != 0]