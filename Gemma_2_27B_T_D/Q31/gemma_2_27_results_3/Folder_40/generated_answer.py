def if_perfect_num(nums):
    sum = 1
    for i in range(2, int(nums[7] ** 0.5) + 1):
        if nums[7] % i == 0:
            sum += i + nums[7] // i
    return sum == nums[7]