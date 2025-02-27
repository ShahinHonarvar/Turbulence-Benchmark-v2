def if_perfect_num(nums):
    if len(nums) > 90:
        sum = 1
        for i in range(2, int(nums[90] ** 0.5) + 1):
            if nums[90] % i == 0:
                sum += i + nums[90] // i
        return sum == nums[90]
    else:
        return False