def if_perfect_num(nums):

    def is_perfect(n):
        divisors = [i for i in range(1, n) if n % i == 0]
        return sum(divisors) == n
    if len(nums) > 28 and nums[28] > 0:
        return is_perfect(nums[28])
    else:
        return False