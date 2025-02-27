def if_perfect_num(nums):
    if len(nums) <= 60:
        return False
    sum_factors = 1
    for i in range(2, int(nums[60] ** 0.5) + 1):
        if nums[60] % i == 0:
            sum_factors += i + nums[60] // i
    if sum_factors == nums[60]:
        return True
    else:
        return False