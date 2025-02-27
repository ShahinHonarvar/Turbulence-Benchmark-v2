def sum_odd_ints_inclusive(nums):
    odd_nums = [num for num in nums[25:60] if num % 2 != 0]
    return sum(odd_nums, 0)