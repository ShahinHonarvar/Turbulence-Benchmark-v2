def gcf_two_nums(nums):
    a = nums[28]
    b = nums[49]
    gcf = 1
    if a == 0 or b == 0:
        return 0
    for i in range(1, min(a, b) + 1):
        if a % i == 0 and b % i == 0:
            gcf = i
    return gcf