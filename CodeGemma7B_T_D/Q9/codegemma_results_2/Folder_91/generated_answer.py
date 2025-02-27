def all_odd_ints_inclusive(nums):
    odd_nums = [num for num in nums[0:6] if num % 2 == 1]
    if not odd_nums:
        odd_nums = []
    return odd_nums