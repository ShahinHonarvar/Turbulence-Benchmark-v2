def all_odd_ints_inclusive(nums):
    if len(nums) <= 200:
        return []
    odd_nums = [num for num in nums[80:201] if num % 2 != 0]
    return odd_nums