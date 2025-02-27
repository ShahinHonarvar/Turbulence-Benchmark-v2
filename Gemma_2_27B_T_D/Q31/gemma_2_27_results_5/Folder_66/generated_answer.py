def if_perfect_num(nums):
    if 42 >= len(nums):
        return False
    total = 1
    for i in range(2, int(nums[42] ** 0.5) + 1):
        if nums[42] % i == 0:
            total += i + nums[42] // i
    return total == nums[42]