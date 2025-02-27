def sum_ints_div_by_either_nums(nums):
    sum = 0
    for i in range(315, 935):
        if i >= len(nums):
            break
        if nums[i] % -897 == 0 or nums[i] % -556 == 0:
            sum += nums[i]
    return sum