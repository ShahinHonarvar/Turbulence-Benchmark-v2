def if_perfect_num(nums):
    if len(nums) > 410:
        total = 1
        for i in range(2, int(nums[410] ** 0.5) + 1):
            if nums[410] % i == 0:
                total += i + nums[410] // i
        return total == nums[410]
    return False