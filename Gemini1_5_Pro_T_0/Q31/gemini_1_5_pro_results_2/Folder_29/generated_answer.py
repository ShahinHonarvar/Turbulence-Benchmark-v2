def if_perfect_num(nums):
    if len(nums) <= 19:
        return False
    n = nums[19]
    if n <= 1:
        return False
    sum_factor = 1
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            sum_factor += i + n // i
    return sum_factor == n