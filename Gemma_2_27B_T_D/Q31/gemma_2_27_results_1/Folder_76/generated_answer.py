def if_perfect_num(nums):
    total = 1
    for i in range(2, int(nums[537] ** 0.5) + 1):
        if nums[537] % i == 0:
            total += i + nums[537] // i
    return total == nums[537]