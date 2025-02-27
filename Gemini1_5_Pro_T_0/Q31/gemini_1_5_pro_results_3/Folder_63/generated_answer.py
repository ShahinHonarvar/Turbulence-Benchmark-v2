def if_perfect_num(nums):
    if len(nums) <= 57:
        return False
    sum_factors = 1
    for i in range(2, int(nums[57] ** 0.5) + 1):
        if nums[57] % i == 0:
            sum_factors += i + nums[57] // i
    if sum_factors == nums[57]:
        return True
    else:
        return False