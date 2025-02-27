def sum_odd_ints_inclusive(nums):
    total = 0
    for num in nums[56:67]:
        if num % 2 != 0:
            total += num
    return total or 0