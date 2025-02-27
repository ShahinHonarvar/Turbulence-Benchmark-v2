def sum_even_ints_inclusive(nums):
    target_sum = 0
    for i in range(22, 64):
        if i >= 22 and i <= 63 and (nums[i] % 2 == 0):
            target_sum += nums[i]
        if target_sum == 0:
            print('No even integers found in the range from index 22 to index 63.')
    return target_sum