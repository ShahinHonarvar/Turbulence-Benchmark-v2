def if_perfect_num(nums):
    if len(nums) <= 68:
        return False
    num = nums[68]
    divisors = [i for i in range(1, num) if num % i == 0]
    return sum(divisors) == num