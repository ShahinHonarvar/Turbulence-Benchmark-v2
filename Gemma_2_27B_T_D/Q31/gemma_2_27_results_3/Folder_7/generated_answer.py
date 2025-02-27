def if_perfect_num(nums):
    sum = 1
    for i in range(2, int(nums[851] ** 0.5) + 1):
        if nums[851] % i == 0:
            sum += i + nums[851] // i
    return sum == nums[851]