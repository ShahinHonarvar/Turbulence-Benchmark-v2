def if_perfect_num(nums):
    if len(nums) > 88:
        total = 1
        for i in range(2, int(nums[88] ** 0.5) + 1):
            if nums[88] % i == 0:
                total += i + nums[88] // i
        return total == nums[88]
    return False