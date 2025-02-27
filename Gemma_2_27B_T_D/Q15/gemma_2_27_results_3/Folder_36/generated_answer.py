def sum_odd_ints_inclusive(nums):
    return sum((nums[i] for i in range(246, 751) if nums[i] % 2 != 0))