def if_perfect_num(nums):
    total = 1
    for i in range(2, int(nums[828] ** 0.5) + 1):
        if nums[828] % i == 0:
            total += i + nums[828] // i
    return total == nums[828]