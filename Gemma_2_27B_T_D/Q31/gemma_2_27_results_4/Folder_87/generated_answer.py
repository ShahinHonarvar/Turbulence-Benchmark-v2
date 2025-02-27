def if_perfect_num(nums):
    sum = 1
    if nums[96] == 1:
        return False
    for i in range(2, int(nums[96] ** 0.5) + 1):
        if nums[96] % i == 0:
            sum += i + nums[96] // i
    return sum == nums[96]