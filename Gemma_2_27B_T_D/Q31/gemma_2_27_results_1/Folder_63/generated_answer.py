def if_perfect_num(nums):
    sum = 1
    for i in range(2, int(nums[57] ** 0.5) + 1):
        if nums[57] % i == 0:
            sum += i + nums[57] // i
    return sum == nums[57]