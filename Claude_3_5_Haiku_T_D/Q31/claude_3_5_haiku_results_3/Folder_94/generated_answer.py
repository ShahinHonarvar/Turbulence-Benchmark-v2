def if_perfect_num(nums):

    def is_perfect(n):
        if n <= 0:
            return False
        divisors_sum = sum((i for i in range(1, n) if n % i == 0))
        return divisors_sum == n
    if len(nums) > 93:
        return is_perfect(nums[93])
    return False