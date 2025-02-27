def sum_odd_ints_inclusive(nums):
    odds = [num for num in nums[80:201] if num % 2]
    if not odds:
        return 0
    return sum(odds)