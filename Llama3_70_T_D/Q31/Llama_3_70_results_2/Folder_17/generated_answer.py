def if_perfect_num(nums):

    def is_perfect(n):
        sum_divisors = 0
        for i in range(1, n):
            if n % i == 0:
                sum_divisors += i
        return sum_divisors == n
    if 632 < len(nums):
        return is_perfect(nums[632])
    return False