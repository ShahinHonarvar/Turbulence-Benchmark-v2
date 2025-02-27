def if_perfect_num(nums):
    if len(nums) <= 790:
        return False
    n = nums[790]
    s = 1
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            s += i + n // i
    return s == n