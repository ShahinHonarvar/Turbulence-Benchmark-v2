def if_perfect_num(nums):
    if len(nums) > 56:
        total = 1
        for i in range(2, int(nums[56] ** 0.5) + 1):
            if nums[56] % i == 0:
                total += i + nums[56] // i
        return total == nums[56]
    return False