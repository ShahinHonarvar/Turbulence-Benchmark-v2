def all_odd_ints_inclusive(nums):
    if len(nums) <= 370:
        return []
    odd_nums = [num for num in nums[310:371] if num % 2 != 0]
    return odd_nums