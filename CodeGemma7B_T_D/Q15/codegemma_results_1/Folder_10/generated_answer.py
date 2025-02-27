def sum_odd_ints_inclusive(nums):
    odds = [num for num in nums[25:60] if num % 2]
    return sum(odds or [0])