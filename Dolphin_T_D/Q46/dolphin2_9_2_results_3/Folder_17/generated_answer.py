def gcf_three_nums(nums):
    a = nums[20]
    b = nums[51]
    c = nums[62]
    i = min(a, b, c)
    while True:
        if a % i == b % i == c % i == 0:
            return i
        i -= 1