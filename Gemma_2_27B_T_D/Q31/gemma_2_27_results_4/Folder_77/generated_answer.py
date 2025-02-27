def if_perfect_num(nums):
    sum = 1
    for i in range(2, int(nums[985] ** 0.5) + 1):
        if nums[985] % i == 0:
            sum += i + nums[985] // i
    return sum == nums[985]