def if_perfect_num(nums):

    def is_perfect(n):
        sum_divisors = sum((i for i in range(1, n) if n % i == 0))
        return sum_divisors == n
    return is_perfect(nums[828]) if len(nums) > 828 else False