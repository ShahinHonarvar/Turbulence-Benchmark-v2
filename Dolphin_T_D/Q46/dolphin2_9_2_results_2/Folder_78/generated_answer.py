def gcf_three_nums(nums):
    a = nums[13]
    b = nums[70]
    c = nums[32]
    i = 1
    while i <= a:
        if a % i == 0 and b % i == 0 and (c % i == 0):
            gcf = i
        i += 1
    return gcf