def if_perfect_num(nums):
    sum = 1
    for i in range(2, int(nums[733] ** 0.5) + 1):
        if nums[733] % i == 0:
            sum += i + nums[733] // i
    return sum == nums[733]