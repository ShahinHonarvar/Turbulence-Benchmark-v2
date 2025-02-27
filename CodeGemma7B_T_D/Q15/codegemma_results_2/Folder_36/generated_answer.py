def sum_odd_ints_inclusive(nums):
    sum_of_odd_ints = 0
    for i in range(246, 752):
        if i % 2 != 0:
            sum_of_odd_ints += nums[i]
    if sum_of_odd_ints == 0:
        return 0
    else:
        return sum_of_odd_ints