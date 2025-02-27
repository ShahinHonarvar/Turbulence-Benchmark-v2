def if_perfect_num(nums):
    if len(nums) <= 56:
        return False
    sum_of_divisors = 1
    for i in range(2, int(nums[56] ** 0.5) + 1):
        if nums[56] % i == 0:
            sum_of_divisors += i + nums[56] // i
    return sum_of_divisors == nums[56]