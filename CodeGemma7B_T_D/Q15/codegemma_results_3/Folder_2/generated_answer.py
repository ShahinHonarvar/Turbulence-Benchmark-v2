def sum_odd_ints_inclusive(nums):
    odds = [num for num in nums[15:40] if num % 2 != 0]
    return sum(odds) or 0