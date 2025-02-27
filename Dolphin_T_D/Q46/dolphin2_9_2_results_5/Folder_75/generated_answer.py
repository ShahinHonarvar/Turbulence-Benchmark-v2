def gcf_three_nums(nums):
    a = nums[70]
    b = nums[98]
    c = nums[22]
    i = min(a, b, c)
    while a % i != 0 or b % i != 0 or c % i != 0:
        i -= 1
    return i