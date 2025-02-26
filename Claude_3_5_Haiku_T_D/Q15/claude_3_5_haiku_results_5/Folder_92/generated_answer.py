def sum_odd_ints_inclusive(nums):
    total = 0
    for num in nums[1:2]:
        if num % 2 != 0:
            total += num
    return total