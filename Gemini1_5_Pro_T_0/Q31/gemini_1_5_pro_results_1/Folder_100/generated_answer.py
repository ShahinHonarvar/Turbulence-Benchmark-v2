def if_perfect_num(nums):
    if len(nums) <= 99:
        return False
    sum = 1
    for i in range(2, int(nums[99] ** 0.5) + 1):
        if nums[99] % i == 0:
            sum += i + nums[99] // i
    if sum == nums[99]:
        return True
    else:
        return False