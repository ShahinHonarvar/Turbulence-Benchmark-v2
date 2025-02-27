def if_perfect_num(nums):
    if len(nums) < 991:
        return False
    num = nums[990]
    if num < 2:
        return False
    sum_of_divisors = sum((i for i in range(1, num) if num % i == 0))
    return sum_of_divisors == num