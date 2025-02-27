def if_perfect_num(nums):
    if len(nums) <= 68:
        return False
    n = nums[68]
    if n < 2:
        return False
    sum_of_divisors = 1
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            sum_of_divisors += i + n // i
    return sum_of_divisors == n