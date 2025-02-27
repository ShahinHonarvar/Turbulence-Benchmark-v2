def if_perfect_num(nums):
    sum = 1
    for i in range(2, int(nums[10] ** 0.5) + 1):
        if nums[10] % i == 0:
            sum += i + nums[10] // i
    return sum == nums[10]