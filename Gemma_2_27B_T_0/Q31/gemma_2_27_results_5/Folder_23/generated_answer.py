def if_perfect_num(nums):
    if len(nums) > 69:
        total = 1
        for i in range(2, int(nums[69] ** 0.5) + 1):
            if nums[69] % i == 0:
                total += i + nums[69] // i
        return total == nums[69]
    return False