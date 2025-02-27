def gcf_two_nums(nums):
    a = nums[6]
    b = nums[9]
    gcf = 1
    for i in range(2, min(a, b) + 1):
        if a % i == 0 and b % i == 0:
            gcf = i
    return gcf