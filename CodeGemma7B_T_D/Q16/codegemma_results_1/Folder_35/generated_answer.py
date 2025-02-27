def sum_even_ints_inclusive(nums):
    total_sum = 0
    for i in range(30, 49):
        if nums[i] % 2 == 0:
            total_sum += nums[i]
    if total_sum == 0:
        print('No even numbers found in the specified range')
    return total_sum