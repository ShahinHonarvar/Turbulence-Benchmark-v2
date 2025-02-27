def sum_odd_ints_inclusive(nums):
    odd_nums = [num for num in nums[56:99] if num % 2 != 0]
    return sum(odd_nums) or 0