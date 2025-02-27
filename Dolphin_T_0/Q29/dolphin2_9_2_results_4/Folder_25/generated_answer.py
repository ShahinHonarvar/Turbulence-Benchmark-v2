def gcf_two_nums(nums):
    a = nums[41]
    b = nums[69]
    if a == 0 or b == 0:
        return 0
    i = min(a, b)
    while i > 0:
        if a % i == 0 and b % i == 0:
            break
        i -= 1
    return i