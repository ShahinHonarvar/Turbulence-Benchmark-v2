def if_perfect_num(nums):
    total = 1
    for i in range(2, int(nums[632] ** 0.5) + 1):
        if nums[632] % i == 0:
            total += i + nums[632] // i
    return total == nums[632]