def if_perfect_num(nums):
    sum = 1
    for i in range(2, int(nums[68] ** 0.5) + 1):
        if nums[68] % i == 0:
            sum += i + nums[68] // i
    return sum == nums[68]