def if_perfect_num(nums):
    if len(nums) <= 95:
        return False
    sum_factors = 1
    for i in range(2, int(nums[95] ** 0.5) + 1):
        if nums[95] % i == 0:
            sum_factors += i + nums[95] // i
    if sum_factors == nums[95]:
        return True
    else:
        return False