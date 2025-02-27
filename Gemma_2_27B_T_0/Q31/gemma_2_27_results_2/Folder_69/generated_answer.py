def if_perfect_num(nums):
    total = 1
    for i in range(2, int(nums[459] ** 0.5) + 1):
        if nums[459] % i == 0:
            total += i + nums[459] // i
    return total == nums[459]