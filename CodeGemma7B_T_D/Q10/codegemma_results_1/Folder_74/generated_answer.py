def all_odd_ints_exclusive(nums):
    odd_nums = [n for n in nums[13:70] if n % 2 != 0]
    return odd_nums if odd_nums else []