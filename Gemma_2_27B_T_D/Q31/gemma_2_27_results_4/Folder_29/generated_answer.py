def if_perfect_num(nums):
    sum = 1
    for i in range(2, int(nums[19] ** 0.5) + 1):
        if nums[19] % i == 0:
            sum += i
            if i != nums[19] // i:
                sum += nums[19] // i
    return sum == nums[19]