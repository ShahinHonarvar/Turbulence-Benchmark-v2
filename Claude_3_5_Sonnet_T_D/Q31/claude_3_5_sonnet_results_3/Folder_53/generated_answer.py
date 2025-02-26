def if_perfect_num(nums):
    if len(nums) <= 73:
        return False
    num = nums[73]
    sum_of_divisors = sum((i for i in range(1, num) if num % i == 0))
    return sum_of_divisors == num