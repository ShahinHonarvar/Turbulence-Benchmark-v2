def all_odd_ints_inclusive(nums):
    odd_nums = [num for num in nums[80:201] if num % 2 != 0]
    if not odd_nums:
        return []
    return odd_nums