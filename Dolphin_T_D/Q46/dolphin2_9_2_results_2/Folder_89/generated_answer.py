def gcf_three_nums(nums):
    a = nums[63]
    b = nums[73]
    c = nums[11]
    gcf = 1
    for i in range(1, min(a, b, c) + 1):
        if a % i == 0 and b % i == 0 and (c % i == 0):
            gcf = i
    return gcf