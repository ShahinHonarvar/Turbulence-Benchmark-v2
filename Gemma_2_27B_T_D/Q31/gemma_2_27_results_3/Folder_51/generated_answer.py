def if_perfect_num(nums):
    sum = 1
    for i in range(2, int(nums[64] ** 0.5) + 1):
        if nums[64] % i == 0:
            sum += i + nums[64] // i
    return sum == nums[64]