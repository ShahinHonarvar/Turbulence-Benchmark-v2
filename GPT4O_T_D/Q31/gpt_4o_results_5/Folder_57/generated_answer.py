def if_perfect_num(nums):
    if len(nums) <= 92:
        return False
    n = nums[92]
    if n <= 1:
        return False
    divisors_sum = 0
    for i in range(1, n):
        if n % i == 0:
            divisors_sum += i
    return divisors_sum == n