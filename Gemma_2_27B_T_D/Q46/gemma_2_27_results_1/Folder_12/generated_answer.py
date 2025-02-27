def gcf_three_nums(nums):
    a = nums[91]
    b = nums[45]
    c = nums[48]
    while True:
        a = min(a, b, c)
        if b % a == 0 and c % a == 0:
            return a
        b = b - a
        c = c - a