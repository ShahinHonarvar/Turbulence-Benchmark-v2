def if_perfect_num(nums):
    sum = 1
    for i in range(2, int(nums[23] ** 0.5) + 1):
        if nums[23] % i == 0:
            sum += i + nums[23] // i
    return sum == nums[23]