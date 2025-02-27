def sum_ints_div_by_either_nums(nums):
    sum = 0
    for i in range(51, 77):
        if i >= len(nums):
            break
        if nums[i] % -90 == 0 or nums[i] % -59 == 0:
            sum += nums[i]
    return sum