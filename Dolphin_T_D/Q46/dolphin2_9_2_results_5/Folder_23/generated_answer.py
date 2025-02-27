def gcf_three_nums(nums):
    a = nums[31]
    b = nums[25]
    c = nums[80]
    gcf = None
    i = 1
    while i <= a:
        if a % i == 0 and b % i == 0 and (c % i == 0):
            gcf = i
        i += 1
    return gcf