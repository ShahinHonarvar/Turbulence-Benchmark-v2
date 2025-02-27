def gcf_three_nums(nums):
    a = nums[93]
    b = nums[94]
    c = nums[57]
    gc = 1
    for i in range(1, max(a, b, c) + 1):
        if a % i == b % i == c % i == 0:
            gc = i
    return gc