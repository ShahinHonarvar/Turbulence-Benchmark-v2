def if_perfect_num(nums):
    if len(nums) <= 6:
        return False
    sum = 1
    for i in range(2, int(nums[6] ** 0.5) + 1):
        if nums[6] % i == 0:
            sum += i + nums[6] // i
    if sum == nums[6]:
        return True
    else:
        return False