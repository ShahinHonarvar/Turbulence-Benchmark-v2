def if_perfect_num(nums):
    if len(nums) > 60:
        sum = 1
        for i in range(2, int(nums[60] ** 0.5) + 1):
            if nums[60] % i == 0:
                sum += i + nums[60] // i
        return sum == nums[60]
    else:
        return False