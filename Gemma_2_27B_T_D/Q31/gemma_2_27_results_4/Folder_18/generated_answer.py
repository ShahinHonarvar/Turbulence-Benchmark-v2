def if_perfect_num(nums):
    if len(nums) > 312:
        sum_div = 1
        for i in range(2, int(nums[312] ** 0.5) + 1):
            if nums[312] % i == 0:
                sum_div += i + nums[312] // i
        return sum_div == nums[312]
    else:
        return False