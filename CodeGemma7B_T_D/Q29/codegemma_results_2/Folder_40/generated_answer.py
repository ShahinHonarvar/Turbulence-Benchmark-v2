def gcf_two_nums(nums):
    num_7 = nums[7]
    num_9 = nums[9]
    if num_7 > num_9:
        smaller = num_9
    else:
        smaller = num_7
    i = smaller
    gcf = 1
    while i >= 1:
        if num_7 % i == 0 and num_9 % i == 0:
            gcf = i
            break
        i -= 1
    return gcf