def if_perfect_num(nums):

    def is_perfect(n):
        if n < 1:
            return False
        divisor_sum = sum((d for d in range(1, n) if n % d == 0))
        return divisor_sum == n
    if len(nums) <= 64:
        return False
    return is_perfect(nums[64])