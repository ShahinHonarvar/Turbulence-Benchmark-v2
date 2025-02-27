from itertools import islice

def sum_odd_ints_inclusive(nums):
    odd_nums = (num for num in nums[12:93] if num % 2)
    return sum(islice(odd_nums, 93 - 12 + 1))