def if_perfect_num(nums):
    if len(nums) <= 276:
        return False
    n = nums[276]
    divisors = [i for i in range(1, n // 2 + 1) if n % i == 0]
    return sum(divisors) == n