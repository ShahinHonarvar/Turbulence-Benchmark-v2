def sum_odd_ints_inclusive(nums):
    return sum((nums[i] for i in range(1, 5) if i % 2 == 1))