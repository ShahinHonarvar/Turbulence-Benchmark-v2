def if_perfect_num(nums):
    total = 1
    for i in range(2, int(nums[990] ** 0.5) + 1):
        if nums[990] % i == 0:
            total += i + nums[990] // i
    return total == nums[990]