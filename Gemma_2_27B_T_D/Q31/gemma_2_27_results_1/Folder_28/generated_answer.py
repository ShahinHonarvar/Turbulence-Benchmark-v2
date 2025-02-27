def if_perfect_num(nums):
    if len(nums) > 37:
        sum = 1
        for i in range(2, int(nums[37] ** 0.5) + 1):
            if nums[37] % i == 0:
                sum += i + nums[37] // i
        return sum == nums[37]
    else:
        return False