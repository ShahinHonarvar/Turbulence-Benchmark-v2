def if_perfect_num(nums):

    def sum_of_factors(n):
        factors = [i for i in range(1, n) if n % i == 0]
        return sum(factors)
    return sum_of_factors(nums[0]) == nums[0]