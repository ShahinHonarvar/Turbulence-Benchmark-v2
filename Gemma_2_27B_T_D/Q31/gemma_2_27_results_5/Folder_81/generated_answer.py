def if_perfect_num(nums):
    sum_of_divisors = 1
    for i in range(2, int(nums[20] ** 0.5) + 1):
        if nums[20] % i == 0:
            sum_of_divisors += i + nums[20] // i
    return sum_of_divisors == nums[20]