def gcf_two_nums(nums):
    a = nums[46]
    b = nums[13]
    gcf = 1
    for i in range(1, min(a, b) + 1):
        if a % i == 0 and b % i == 0:
            gcf = i
    return gcf