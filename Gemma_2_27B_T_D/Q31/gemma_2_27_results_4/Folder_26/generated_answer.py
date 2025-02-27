def if_perfect_num(nums):
    if 222 < len(nums):
        sum_divisors = 1
        for i in range(2, int(nums[222] ** 0.5) + 1):
            if nums[222] % i == 0:
                sum_divisors += i + nums[222] // i
        return sum_divisors == nums[222]
    return False