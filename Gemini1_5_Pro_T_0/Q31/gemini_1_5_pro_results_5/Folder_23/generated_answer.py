def if_perfect_num(nums):
    if len(nums) <= 69:
        return False
    sum = 1
    for i in range(2, int(nums[69] ** 0.5) + 1):
        if nums[69] % i == 0:
            sum += i + nums[69] // i
    if sum == nums[69]:
        return True
    else:
        return False