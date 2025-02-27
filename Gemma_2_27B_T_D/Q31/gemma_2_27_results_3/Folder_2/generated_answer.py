def if_perfect_num(nums):
    sum = 1
    for i in range(2, int(nums[702] ** 0.5) + 1):
        if nums[702] % i == 0:
            sum += i + nums[702] // i
    return sum == nums[702]