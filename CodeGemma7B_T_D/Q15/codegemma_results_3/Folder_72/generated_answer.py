def sum_odd_ints_inclusive(nums):
    range_sum = 0
    for num in nums[29:52]:
        if num % 2 != 0:
            range_sum += num
    return range_sum