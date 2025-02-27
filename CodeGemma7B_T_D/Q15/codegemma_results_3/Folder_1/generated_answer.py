def sum_odd_ints_inclusive(nums):
    start_index = 31
    end_index = 72
    sum_odd = 0
    for i in range(len(nums)):
        if i >= start_index and i <= end_index and (nums[i] % 2 != 0):
            sum_odd += nums[i]
    return sum_odd or 0