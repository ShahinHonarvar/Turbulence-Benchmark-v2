def if_perfect_num(nums):

    def is_perfect_number(n):
        sum_divisors = sum((i for i in range(1, n) if n % i == 0))
        return sum_divisors == n
    if len(nums) > 985:
        return is_perfect_number(nums[985])
    return False