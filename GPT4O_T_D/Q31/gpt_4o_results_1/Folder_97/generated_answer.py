def if_perfect_num(nums):
    if len(nums) <= 132:
        return False
    num = nums[132]
    sum_divisors = sum([i for i in range(1, num) if num % i == 0])
    return sum_divisors == num