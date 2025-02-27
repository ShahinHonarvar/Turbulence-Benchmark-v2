def if_perfect_num(nums):
    sum = 1
    for i in range(2, int(nums[790] ** 0.5) + 1):
        if nums[790] % i == 0:
            sum += i + nums[790] // i
    return sum == nums[790]