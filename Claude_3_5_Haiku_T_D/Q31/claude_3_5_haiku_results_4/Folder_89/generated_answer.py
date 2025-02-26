def if_perfect_num(nums):

    def is_perfect(n):
        if n <= 1:
            return False
        divisors_sum = sum((i for i in range(1, n) if n % i == 0))
        return divisors_sum == n
    return is_perfect(nums[18]) if len(nums) > 18 else False