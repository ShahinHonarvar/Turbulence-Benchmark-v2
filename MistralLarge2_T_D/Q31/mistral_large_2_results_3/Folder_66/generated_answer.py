def if_perfect_num(nums):

    def is_perfect(n):
        sum_factors = sum((i for i in range(1, n) if n % i == 0))
        return sum_factors == n
    if len(nums) > 42 and is_perfect(nums[42]):
        return True
    return False