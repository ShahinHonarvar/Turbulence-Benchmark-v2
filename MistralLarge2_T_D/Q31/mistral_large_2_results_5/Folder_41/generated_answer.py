def if_perfect_num(nums):

    def is_perfect(n):
        sum_of_factors = sum((i for i in range(1, n) if n % i == 0))
        return sum_of_factors == n
    return is_perfect(nums[84]) if len(nums) > 84 else False