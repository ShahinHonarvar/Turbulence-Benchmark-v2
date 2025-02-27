def gcf_two_nums(nums):
    num_a = nums[85]
    num_b = nums[51]
    if num_a > num_b:
        smaller = num_b
    else:
        smaller = num_a
    while num_b != 0:
        temp = num_b
        num_b = num_a % num_b
        num_a = temp
    return num_a