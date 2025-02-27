def if_perfect_num(nums):
    if 27 < len(nums):
        n = nums[27]
        sum_divisors = 1
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                sum_divisors += i + n // i
        return sum_divisors == n
    return False