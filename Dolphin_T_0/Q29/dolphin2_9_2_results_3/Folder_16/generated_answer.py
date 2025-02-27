def gcf_two_nums(nums):
    a, b = (nums[860], nums[307])
    a, b = (min(a, b), max(a, b))
    while b % a:
        a, b = (b % a, a)
    return a