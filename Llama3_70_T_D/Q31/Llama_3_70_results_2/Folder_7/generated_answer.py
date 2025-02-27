def if_perfect_num(nums):

    def sum_of_divisors(n):
        return sum([i for i in range(1, n) if n % i == 0])
    return sum_of_divisors(nums[851]) == nums[851]