def gcf_three_nums(nums):
    a = nums[24]
    b = nums[25]
    c = nums[80]
    while True:
        if a < b:
            a, b = (b, a)
        if b == 0:
            return a
        a %= b