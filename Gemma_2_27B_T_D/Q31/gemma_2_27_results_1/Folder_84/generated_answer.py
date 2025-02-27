def if_perfect_num(nums):
    sum = 1
    for i in range(2, int(nums[685] ** 0.5) + 1):
        if nums[685] % i == 0:
            sum += i + nums[685] // i
    return sum == nums[685]