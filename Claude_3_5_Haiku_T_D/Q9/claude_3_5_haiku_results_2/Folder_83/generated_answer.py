def all_odd_ints_inclusive(nums):
    if len(nums) < 201:
        return []
    return [num for num in nums[90:201] if num % 2 != 0]