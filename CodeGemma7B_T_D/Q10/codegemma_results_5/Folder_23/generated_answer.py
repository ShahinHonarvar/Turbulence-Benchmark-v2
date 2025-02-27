def all_odd_ints_exclusive(nums):
    odd_nums = [num for num in nums[29:54] if num % 2 != 0]
    return odd_nums if odd_nums else []