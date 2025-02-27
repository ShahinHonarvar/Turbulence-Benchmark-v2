def if_perfect_num(nums):
    if len(nums) > 15:
        sum = 1
        for i in range(2, int(nums[15] ** 0.5) + 1):
            if nums[15] % i == 0:
                sum += i + nums[15] // i
        return sum == nums[15]
    else:
        return False