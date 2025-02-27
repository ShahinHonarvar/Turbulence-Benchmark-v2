def if_perfect_num(nums):
    if len(nums) > 100:
        total = 1
        for i in range(2, int(nums[100] ** 0.5) + 1):
            if nums[100] % i == 0:
                total += i + nums[100] // i
        return total == nums[100]
    else:
        return False