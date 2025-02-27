def if_perfect_num(nums):
    if len(nums) > 54:
        sum_divisors = 1
        for i in range(2, int(nums[54] ** 0.5) + 1):
            if nums[54] % i == 0:
                sum_divisors += i + nums[54] // i
        return sum_divisors == nums[54]
    return False