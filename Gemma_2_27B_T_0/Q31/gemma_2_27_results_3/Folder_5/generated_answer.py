def if_perfect_num(nums):
    if len(nums) > 67:
        sum = 1
        for i in range(2, int(nums[67] ** 0.5) + 1):
            if nums[67] % i == 0:
                sum += i + nums[67] // i
        return sum == nums[67]
    return False