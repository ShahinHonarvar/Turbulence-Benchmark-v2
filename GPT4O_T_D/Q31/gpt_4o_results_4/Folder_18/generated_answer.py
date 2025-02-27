def if_perfect_num(nums):
    if len(nums) <= 312:
        return False
    num = nums[312]
    divisors = [i for i in range(1, num) if num % i == 0]
    return sum(divisors) == num