def if_perfect_num(nums):
    sum = 1
    for i in range(2, int(nums[247] ** 0.5) + 1):
        if nums[247] % i == 0:
            sum += i + nums[247] // i
    return sum == nums[247]