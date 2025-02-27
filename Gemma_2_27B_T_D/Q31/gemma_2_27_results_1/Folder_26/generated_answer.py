def if_perfect_num(nums):
    sum = 1
    for i in range(2, int(nums[222] ** 0.5) + 1):
        if nums[222] % i == 0:
            sum += i + nums[222] // i
    return sum == nums[222]