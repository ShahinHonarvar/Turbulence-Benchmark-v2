def all_odd_ints_inclusive(nums):
    if len(nums) < 92:
        return []
    odd_nums = [num for num in nums[11:93] if num % 2 != 0]
    return odd_nums