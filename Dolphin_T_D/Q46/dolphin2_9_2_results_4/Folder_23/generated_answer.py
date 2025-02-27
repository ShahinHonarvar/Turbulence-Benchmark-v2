def gcf_three_nums(nums):
    a = nums[31]
    b = nums[25]
    c = nums[80]
    i = min(a, b, c)
    while i >= 1:
        if a % i == 0 and b % i == 0 and (c % i == 0):
            return i
        i -= 1
    return 1