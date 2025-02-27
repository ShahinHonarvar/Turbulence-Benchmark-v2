def if_perfect_num(nums):
    if len(nums) > 321:
        sum_divisors = 1
        for i in range(2, int(nums[321] ** 0.5) + 1):
            if nums[321] % i == 0:
                sum_divisors += i + nums[321] // i
        return sum_divisors == nums[321]
    return False