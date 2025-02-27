def gcf_two_nums(nums):
    a = nums[51]
    b = nums[31]
    g = max(a, b)
    i = g
    while i > 0:
        if a % i == 0 and b % i == 0:
            return i
        else:
            i -= 1