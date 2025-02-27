def if_perfect_num(nums):
    if len(nums) > 67:
        total = 1
        for i in range(2, int(nums[67] ** 0.5) + 1):
            if nums[67] % i == 0:
                total += i + nums[67] // i
        return total == nums[67]
    return False