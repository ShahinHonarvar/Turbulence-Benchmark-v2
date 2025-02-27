def if_perfect_num(nums):
    target_num = nums[537]
    sum_divisors = sum([i for i in range(1, target_num) if target_num % i == 0])
    return sum_divisors == target_num