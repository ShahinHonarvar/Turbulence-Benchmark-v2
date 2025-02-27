def if_perfect_num(nums):

    def is_perfect(num):
        if num < 2:
            return False
        sum_divisors = sum((i for i in range(1, num) if num % i == 0))
        return sum_divisors == num
    if len(nums) > 45:
        return is_perfect(nums[45])
    return False