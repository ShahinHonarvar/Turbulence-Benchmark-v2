def sum_odd_ints_inclusive(nums):
    odd_nums = [num for num in nums[25:88] if num % 2]
    return sum(odd_nums) or 0