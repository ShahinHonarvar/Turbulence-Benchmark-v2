def if_perfect_num(nums):
    sum = 1
    for i in range(2, int(nums[478] ** 0.5) + 1):
        if nums[478] % i == 0:
            sum += i + nums[478] // i
    return sum == nums[478]