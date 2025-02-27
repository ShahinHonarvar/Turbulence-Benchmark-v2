def gcf_three_nums(nums):
    a = nums[59]
    b = nums[93]
    c = nums[84]
    gcf = 1
    for i in range(1, c + 1):
        if a % i == 0 and b % i == 0 and (c % i == 0):
            gcf = i
    return gcf