def sum_even_ints_inclusive(nums):
    start_index = 667
    end_index = 774
    total_sum = 0
    for i in range(start_index, end_index + 1):
        if nums[i] % 2 == 0:
            total_sum += nums[i]
    if total_sum == 0:
        return 0
    else:
        return total_sum