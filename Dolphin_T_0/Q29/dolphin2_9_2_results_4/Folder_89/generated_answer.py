def gcf_two_nums(nums):
    a = nums[37]
    b = nums[30]
    i = min(a, b)
    while i > 0:
        if a % i == 0 and b % i == 0:
            return i
        i -= 1
    return 1