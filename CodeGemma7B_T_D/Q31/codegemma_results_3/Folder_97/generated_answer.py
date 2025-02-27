def if_perfect_num(nums):
    num = nums[131]
    sum_of_divisors = sum((i for i in range(1, num + 1) if num % i == 0))
    return sum_of_divisors == num