def gcf_three_nums(nums):
    a = nums[876]
    b = nums[203]
    c = nums[100]
    i = min(a, b, c)
    while i > 1:
        if a % i == b % i == c % i == 0:
            return i
        i -= 1
    return 1