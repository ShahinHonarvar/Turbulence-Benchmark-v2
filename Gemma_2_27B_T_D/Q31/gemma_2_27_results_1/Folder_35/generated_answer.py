def if_perfect_num(nums):
    sum = 1
    for i in range(2, int(nums[993] ** 0.5) + 1):
        if nums[993] % i == 0:
            sum += i + nums[993] // i
    return sum == nums[993]