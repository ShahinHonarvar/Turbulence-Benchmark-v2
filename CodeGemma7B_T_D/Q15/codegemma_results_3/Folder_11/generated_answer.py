def sum_odd_ints_inclusive(nums):
    odd_nums = [n for n in nums[37:52] if n % 2 != 0]
    return sum(odd_nums) if odd_nums else 0