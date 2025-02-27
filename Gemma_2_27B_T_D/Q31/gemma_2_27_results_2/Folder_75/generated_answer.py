def if_perfect_num(nums):
    if 80 < len(nums):
        sum_divisors = 1
        for i in range(2, int(nums[80] ** 0.5) + 1):
            if nums[80] % i == 0:
                sum_divisors += i + nums[80] // i
        return sum_divisors == nums[80]
    return False