def gcf_three_nums(nums):
    a = nums[99]
    b = nums[28]
    c = nums[53]
    i = 1
    while i <= a or i <= b or i <= c:
        if a % i == 0 and b % i == 0 and (c % i == 0):
            gcf = i
        i += 1
    return gcf