def if_perfect_num(nums):
    sum = 1
    for i in range(2, int(nums[453] ** 0.5) + 1):
        if nums[453] % i == 0:
            sum += i + nums[453] // i
    return sum == nums[453]