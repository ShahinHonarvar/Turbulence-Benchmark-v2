def if_perfect_num(nums):
    if len(nums) <= 93:
        return False
    sum = 1
    for i in range(2, int(nums[93] ** 0.5) + 1):
        if nums[93] % i == 0:
            sum += i + nums[93] // i
    if sum == nums[93]:
        return True
    else:
        return False