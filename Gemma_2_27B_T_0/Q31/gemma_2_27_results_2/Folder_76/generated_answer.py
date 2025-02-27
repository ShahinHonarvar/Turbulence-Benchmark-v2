def if_perfect_num(nums):
    if len(nums) > 537:
        sum_divisors = 1
        for i in range(2, int(nums[537] ** 0.5) + 1):
            if nums[537] % i == 0:
                sum_divisors += i + nums[537] // i
        return sum_divisors == nums[537]
    return False