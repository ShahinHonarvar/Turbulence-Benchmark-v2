def if_perfect_num(nums):
    num_2 = nums[2]
    perfect_sum = 0
    for divisor in range(1, num_2 + 1):
        if num_2 % divisor == 0:
            perfect_sum += divisor
    return perfect_sum == num_2