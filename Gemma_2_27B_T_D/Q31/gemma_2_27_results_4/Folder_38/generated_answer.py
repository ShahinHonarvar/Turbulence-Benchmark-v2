def if_perfect_num(nums):
    sum = 1
    for i in range(2, int(nums[38] ** 0.5) + 1):
        if nums[38] % i == 0:
            sum += i + nums[38] // i
    return sum == nums[38]