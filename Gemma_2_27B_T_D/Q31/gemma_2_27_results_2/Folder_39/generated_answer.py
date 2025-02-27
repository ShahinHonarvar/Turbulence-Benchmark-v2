def if_perfect_num(nums):
    if len(nums) > 59:
        sum = 1
        for i in range(2, int(nums[59] ** 0.5) + 1):
            if nums[59] % i == 0:
                sum += i + nums[59] // i
        return sum == nums[59]
    return False