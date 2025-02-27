def if_perfect_num(nums):
    if len(nums) <= 51:
        return False
    sum = 1
    for i in range(2, int(nums[51] ** 0.5) + 1):
        if nums[51] % i == 0:
            sum += i + nums[51] // i
    if sum == nums[51]:
        return True
    else:
        return False