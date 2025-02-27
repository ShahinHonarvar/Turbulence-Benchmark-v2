def gcf_three_nums(nums):
    a = nums[637]
    b = nums[411]
    c = nums[757]
    gcf = a
    for i in range(2, min(a, b, c) + 1):
        if a % i == 0 and b % i == 0 and (c % i == 0):
            gcf = i
    return gcf