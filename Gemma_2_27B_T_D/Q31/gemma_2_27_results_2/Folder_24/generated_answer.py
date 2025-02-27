def if_perfect_num(nums):
    sum_of_factors = 1
    for i in range(2, int(nums[74] ** 0.5) + 1):
        if nums[74] % i == 0:
            sum_of_factors += i + nums[74] // i
    return sum_of_factors == nums[74]