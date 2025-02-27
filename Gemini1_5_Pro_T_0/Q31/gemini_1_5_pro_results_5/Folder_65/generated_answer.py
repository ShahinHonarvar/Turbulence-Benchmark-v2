def if_perfect_num(nums):
    if len(nums) <= 35:
        return False
    n = nums[35]
    if n <= 1:
        return False
    sum_of_div = 1
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            sum_of_div += i + n // i
    return sum_of_div == n