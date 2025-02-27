def if_perfect_num(nums):
    if nums[59] == 0:
        return False
    sum_div = 0
    for i in range(1, nums[59]):
        if nums[59] % i == 0:
            sum_div += i
    return sum_div == nums[59]