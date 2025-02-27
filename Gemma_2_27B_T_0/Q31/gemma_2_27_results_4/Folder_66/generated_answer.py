def if_perfect_num(nums):
    if len(nums) > 42:
        total = 1
        for i in range(2, int(nums[42] ** 0.5) + 1):
            if nums[42] % i == 0:
                total += i + nums[42] // i
        return total == nums[42]
    return False