def if_perfect_num(nums):
    if len(nums) > 702:
        sum_divisors = 1
        for i in range(2, int(nums[702] ** 0.5) + 1):
            if nums[702] % i == 0:
                sum_divisors += i + nums[702] // i
        return sum_divisors == nums[702]
    else:
        return False