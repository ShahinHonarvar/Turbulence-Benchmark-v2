def gcf_three_nums(nums):
    a = nums[19]
    b = nums[69]
    c = nums[97]
    gcf = 1
    for i in range(1, a + 1):
        if a % i == 0 and b % i == 0 and (c % i == 0):
            gcf = i
    return gcf