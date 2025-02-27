def if_perfect_num(nums):

    def sum_divisors(n):
        return sum((i for i in range(1, n) if n % i == 0))
    return sum_divisors(nums[0]) == nums[0]