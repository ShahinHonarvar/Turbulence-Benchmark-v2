def if_perfect_num(nums):
    if len(nums) > 100:
        sum_div = 1
        for i in range(2, int(nums[100] ** 0.5) + 1):
            if nums[100] % i == 0:
                sum_div += i + nums[100] // i
        return sum_div == nums[100]
    else:
        return False