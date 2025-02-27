def if_perfect_num(nums):
    if len(nums) <= 60:
        return False
    total = 1
    for i in range(2, int(nums[60] ** 0.5) + 1):
        if nums[60] % i == 0:
            total += i + nums[60] // i
    return total == nums[60]