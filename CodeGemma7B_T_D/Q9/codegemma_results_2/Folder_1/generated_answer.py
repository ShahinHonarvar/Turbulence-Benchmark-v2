def all_odd_ints_inclusive(nums):
    odd_nums = [n for n in nums[31:73] if n % 2 != 0]
    return odd_nums if odd_nums else []