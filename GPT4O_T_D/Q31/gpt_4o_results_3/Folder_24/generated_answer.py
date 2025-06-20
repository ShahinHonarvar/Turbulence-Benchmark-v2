def if_perfect_num(nums):
    if len(nums) <= 74:
        return False

    def is_perfect(n):
        divisors_sum = sum((i for i in range(1, n) if n % i == 0))
        return divisors_sum == n
    return is_perfect(nums[74])