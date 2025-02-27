def sum_odd_ints_inclusive(nums):
    sum = 0
    true_count = 0
    for i in range(33, 37):
        if nums[i] % 2 != 0:
            true_count += 1
            sum += nums[i]
    if true_count == 0:
        return 0
    return sum