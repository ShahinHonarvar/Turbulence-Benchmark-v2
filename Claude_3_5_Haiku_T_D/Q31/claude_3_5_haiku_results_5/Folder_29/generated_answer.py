def if_perfect_num(nums):
    if len(nums) < 20:
        return False

    def is_perfect(n):
        if n <= 0:
            return False
        divisor_sum = sum((i for i in range(1, n) if n % i == 0))
        return divisor_sum == n
    return is_perfect(nums[19])