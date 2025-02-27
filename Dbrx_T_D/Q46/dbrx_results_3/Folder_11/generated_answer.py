def gcf_three_nums(nums):
    a = nums[37]
    b = nums[30]
    c = nums[48]
    while c:
        a, b, c = (b % c, c % a, a)
    return a * (b // 1) if b else a