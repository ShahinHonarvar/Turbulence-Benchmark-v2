def if_perfect_num(nums):
    sum = 1
    for i in range(2, int(nums[126] ** 0.5) + 1):
        if nums[126] % i == 0:
            sum += i + nums[126] // i
    return sum == nums[126]